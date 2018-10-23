# -*- coding: utf-8 -*-
# @Author: chenxinma
# @Date:   2018-07-23 18:43:49
# @Last Modified by:   chenxinma
# @Last Modified at:   2018-07-25 20:03:09

"""
“哪些SKU容易被一起购买？”是一个有趣而重要的问题，SKU关联度在供应链管理中也有很多应用。
SimRank算法是PageRank算法的一个变种，应用于网页排名、协同过滤、孤立点检测、网络图聚类等。一句话概括其思想：如果两个对象和被其相似的对象所引用（即它们有相似的入邻边结构），那么这两个对象也相似。
换句话说，如果我们利用订单数据中的多SKU订单构建一个网络，每个节点代表一个SKU，每条边代表不同SKU是否更可能被一起购买，那么SimRank算法就可以帮助我们得到SKU之间的关联。但是百万级别的SKU数量带来的计算量太大，本页将简化讨论SimRank算法在二级品类的层次上的探索。

SimRank算法本质上是矩阵向量的相乘，利用Spark可在map-reduce框架下实现较高效的并行，代码如下:
"""


import datetime, random
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import numpy as np
import pandas as pd
import scipy.sparse as sps
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.linalg import SparseVector
from pyspark.mllib.regression import LabeledPoint
import csv

from pyspark import SparkContext, SparkConf, HiveContext, sql

appName = 'SimRank'
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)
sqlContext = sql.SQLContext(sc)


def parsePoint(line):
    line = line.split(',')
    label = int(line[0])
    linksTo = list(set(line[1:]))

    NNZ = len(linksTo)
    index = []
    values = []
    if label in [121, 141, 151]:
        return LabeledPoint(label, SparseVector(1, sorted([200]), [1.0]))
    for e in linksTo:
        index += [int(e)]
        values += [1 / (NNZ + 0.0)]

    return LabeledPoint(label, SparseVector(NNZ, sorted(index), values))


def doMultiplication(labeledPoint):
    out = []

    label = labeledPoint.label
    sparseVector = labeledPoint.features

    if sparseVector.size > 0:
        ri = r[int(labeledPoint.label)]
        value = ri * sparseVector.values[0]
        for rowId in sparseVector.indices:
            if rowId < totalPages:
                out += [[rowId, value]]

    return out


if __name__ == "__main__":
    index, batchsize = sys.argv[1], sys.argv[2]
    linkData = sc.textFile("hdfs://ns15/user/cmo_ipc/schemmy/network.txt").map(parsePoint)

    index = int(index)
    batchsize = int(batchsize)
    # totalPages = linkData.map(lambda a: a.label).reduce(max)
    # totalPages = int(totalPages+1)
    # print ("Total catogories %i" %totalPages)
    totalPages = 4389614

    for starting in range(batchsize):
        r = np.zeros(totalPages)
        st = starting + index * batchsize
        print(st)
        r[st] = 1.0

        beta = 0.8
        secondPart = r * (1 - beta)
        linkData.cache()  # to have faster computation

        for it in xrange(10):
            # print "Iteration ",it
            newdata = linkData.flatMap(doMultiplication)
            reducedData = newdata.reduceByKey(lambda a, b: a + b).collect()
            r = np.zeros(totalPages)
            for k, v in reducedData:
                r[k] = v * beta
            r = r + secondPart
            # print r

        rOrig = r.copy()
        top = 50
        B = np.zeros(top, int)
        for i in xrange(top):
            idx = np.argmax(r)
            B[i] = idx;
            r[idx] = 0

        # dic={}
        # f = open('catgDic.txt')
        # for line in f:
        #     lines = line.split(',')
        #     dic[int(lines[1][:-1])] = lines[0]
        # f.close()

        # catgoDic={}
        # f = open('catg.txt')
        # for line in f:
        #     lines = line.split(' ')
        #     lines[-1] = lines[-1].rstrip()
        #     catgoDic[lines[0]] = '_'.join(lines[1:])

        # name = 'edge'+str(index+1)+'.txt'
        # edge = open(name, 'a')
        res = []
        for i in xrange(top):
            if i == 0:
                bm = rOrig[B[i]]
            if i > 0 and B[i] < 152:
                if rOrig[B[i]] > bm / 300:
                    res.append([int(st), int(B[i]), float(rOrig[B[i]])])
                    # edge.write('%d,%d,%f\n' %(st, B[i], rOrig[B[i]]))
        # edge.close()

        df_rdd = sqlContext.createDataFrame(res)
        df_rdd.rdd.map(tuple).saveAsTextFile('hdfs://ns15/user/cmo_ipc/schemmy/simrank_res/res_%i' % int(st))

