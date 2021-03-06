# 创建

### 创建数据框
1. 通过二维数组创建数据框
```python
arr1 = np.array(np.arange(12)).reshape(4,3)
arr1````````
type(arr1)
df1 = pd.DataFrame(arr1)
df1
type(df1)
```
2. 通过字典方式创建数据框
```python
dic1 = {'a':[1,2,3,4],'b':[5,6,7,8],
        'c':[9,10,11,12],'d':[13,14,15,16]}
dic1
type(dic1)
df2 = pd.DataFrame(dic1)
df2
type(df2)
dic2 = {'one':{'a':1,'b':2,'c':3,'d':4},
        'two':{'a':5,'b':6,'c':7,'d':8},
        'three':{'a':9,'b':10,'c':11,'d':12}}
dic2
type(dic2)
df3 = pd.DataFrame(dic2)
df3
type(df3)
```
3. 通过数据框方式创建数据框
```python
df4 = df3[['one','three']] ## 双[[]]保持数据结构
df4
type(df4)
s1 = df3['one'] ## 单[]取成子结构
s1
type(s1)
```

4. 创建一个空的数据框，在按列往里面填数
```python
df5 = pd.DataFrame()
df5['A'] = [1,2,3,4,5]
df5['B'] = range(5)
df5['C'] = np.arrange(5)
```

### 创建序列
1. pandas中有两类非常重要的类
> Series: 一维数组, 数据框中的某列

> DataFrame: 数据框

2. 通过一维数组创建序列
```python
import numpy as np, pandas as pd
arr1 = np.arange(10)
arr1
type(arr1)
s2 = pd.Series(arr1)
s2
type(s2)
```
3. 通过字典方式创建序列
```python
dic1 = {'a':10,'b':20,'c':30,'d':40,'e':50}
dic1
type(dic1)
s3 = pd.Series(dic1)
s3
type(s3)
```

4. 直接创建
```python
x = pd.Series([1,2,3], index=['one', 'two', 'three'])
```

### 读取数据成为数据框
1. 从`.csv`中读取数据
> `pandas.read_csv('testdata.csv',sep=',',parse_dates=['order_date'])` 
> `pd.io.parsers.read_csv()`
> - 从csv中读取时，默认的`sep=','`
> - `parse_dates`可以把有日期的列分解成 年，月，日三列

[更多参数信息](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)



2. 从`.txt`中读取数据
> `pandas.read_table('testdata.txt',sep='\t',parse_dates=['order_date'])` 

# 引用

1. 引用某些列
```python
dic2 = {'a':[1,2,3,4],'b':[5,6,7,8],
        'c':[9,10,11,12],'d':[13,14,15,16]}
df2 = pd.DataFrame(dic2)
df2.columns = ['aaa','bbb','ccc','ddd'] ## 重命名列名

# 第一种引用方式
df2[['aaa','ddd']] ## 双层[[]]保证取出来的数据依然是数据框

# 第二种引用方式
df2.loc[:,['aaa','ddd']] ## 不指定行是不行的

# 第三种引用方式
df2.iloc[:,[0,1]] ## 没有双层的括号取出来的数据类型为Series, 不指定行是不行的
```


2. 引用某些行
```python
dic2 = {'a':[1,2,3,4],'b':[5,6,7,8],
        'c':[9,10,11,12],'d':[13,14,15,16]}
df2 = pd.DataFrame(dic2)
df2.index = ['aaa','bbb','ccc','ddd'] ## 重命名行名

df2.loc[['aaa','ddd']] ## 双层[[]]保证取出来的数据依然数据框

df2.loc[df2.index[[0,1]],:] ## 双层[[]]保证取出来的数据依然数据框, 可以不指定列:df2.loc[df2.index[[0,1]]]

df2.iloc[[0,1],:] ## 双层[[]]保证取出来的数据依然数据框,可以不指定列:df2.iloc[[0,1],:]
```
3. 同时引用某些行和某些列
```python
import numpy as np
import pandas as pd
df = pd.DataFrame(np.arange(0,60,2).reshape(10,3),columns=list('abc'))

# 第一种获取方式(需要提供行名和列名)
df.loc[0, 'a']  #如果想要取出来度数据结构还是数据框, 需要使用df.loc[[0], ['a']]
df.loc[0:3, ['a', 'b']]
df.loc[[1, 5], ['b', 'c']]

# 第二种获取方式(需要提供行号和列号)
df.iloc[1,1]
df.iloc[0:3, [0,1]]
df.iloc[[0, 3, 5], 0:2]
```

---

# 数据框相关基本操作

### 1. 查看数据框的基本信息


1. 查看数据框基本信息
> - `df.info()` 查看基本信息
> - `df.describe()` 查看每列的统计信息

2. 查看各列的数据属性`print(df.dtypes)`
3. 查看列名
> - `df.columns.tolist()`

> - `list(df)`

4. 查看行名`df.index.tolist()`

5. 查看维度信息`df.shape`
> 查看行数`df.shape[0]` or `len(df)`

> 查看列数`df.shape[1]`

6. 判定数据类型是否为数据框
> `df.__class__.__name__=='DataFrame'`

7. 统计某一列每种类型有多少行数据
`df['animal'].value_counts()`








### 2. 基本操作
1. 删除某一行或者某一列
> 1. 删除某些行
> - `df = df.drop(11)`
> - `df.drop([11,12],inplace='True')`

> 2. 删除某些列
> - `df.drop('sku_id',axis=1,inplace='True')`
> - `del df['sku_id']`
> - `spring = df.pop('spring')` 在df中删除了相应的列, 存到了spring中


2. 按某一行正序, 另一行倒序排列
`df.sort_values(by=['age', 'visits'], ascending=[False, True])`

3. 重命名列明
`df.rename(index=str, columns={"colA_old": "colA_new", "colC_old": "colC_new"})`
> 通过columns给出一个替换额字典，据此替换

4. 把某列的数值批量替换
> 把某一个值替换
> - `df['animal'] = df['animal'].replace('snake', 'python')`
> 把多个值对应替换
> - `df['priority'] = df['priority'].map({'yes': True, 'no': False})`

5. 删除重复的行
`df.drop_duplicates()`
> `df.drop_duplicates(keep='first')` 遇到重复时, 只留下第一个数据
> `df.drop_duplicates(keep='last')` 遇到重复时, 只留下最后一个数据
> `df.drop_duplicates(keep='False')` 遇到重复时, 一个数据也不留下

6. 留下重复的行
`df.duplicated()` 返回是否是重复数据的标识: TRUE or FALSE
> `df.duplicated(keep='first')` 遇到重复时,第一个数还是记为false
> `df.duplicated(keep='last')` 遇到重复时, 最后一数还是记为false
> `df.duplicated(keep='False')` 遇到重复时, 统统记为true

7. 取得最大或者最小的数所在的下标(R中`which.min()`)
`df.sum(axis=0).idxmin()` 按列求和,然后去最小的列和的列号
`df.sum(axis=1).idxmax()` 按行求和,然后去最大的行和的行号

8. 透视表功能
`df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')`

9. 一个数据框减去一个列向量
`df.sub(df.mean(axis=1), axis=0)`
> - `df.mean(axis=1)`是求对每行求平均,相当于作用于每行上的运算是一致的
> - `df.mean(axis=0)`是对某一列求平均,相当于作用于每列上的运算是一致的
> - `df.sub([1,2,3,4,5],axis=0)`是每列都去减掉这个list, list的长度必须与df的行长度一致
> - `df.sub([1,2,3],axis=1)`是每行都去减掉这个list, list的长度必须与df的列长度一致

10. 按照每列或者每行累加数据, 得到一个大小一样数据框
`df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))`
> - `df.cumsum(axis=1)` 一列一列的累加, 相当于作用于每行上的运算是一致的
> - `df.cumsum(axis=0)` 一行一行的累加, 相当于作用于每列上的运算是一致的

11. 按照某列分组, 按照另一列的数值排序, 每组取出前3个数
```python
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
df.groupby('grps')['vals'].nlargest(3)  # 每组都取出最大的3个
df.groupby('grps')['vals'].nsmallest(3)  # 每组都取出最小的3个
```

12. 按照某列分组, 按照另一列的数值排序, 每组取出前3个数, 并且求和
```python
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
df.groupby('grps')['vals'].nlargest(3).sum(level=0)  # 每组都取出最大的3个并且组内求和
df.groupby('grps')['vals'].nlargest(3).sum()# 每组都取出最小的3个,并且全部求和
```
> - `level`是用来处理有层次关系的df数据, 从外层往内层求和
> - 默认`level=None`


13. 按照某一列的数据分段分组
```python
## 生成数据框, 其中A列是[1,100]之间的随机整数, B列是从标准正态分布中取数
df = pd.DataFrame({'A': np.random.randint(101,size=200), 
                   'B': np.random.normal(loc=0.0, scale=1.0, size=200)})
## 把A按照(0, 10], (10, 20], ...分组, 然后把对应的组中的B的值求和
df.groupby(pd.cut(df['A'], np.arange(0, 101, 10)))['B'].sum()

# 1. 生成左开右闭的区间: np.arange(0, 101, 10)
# 2. 把df的A列的数值映射到划分好的区间中: pd.cut(df['A'], np.arange(0, 101, 10))
# 3. 按照划分好的区间的标记分组对B中的数值求和: df.groupby(pd.cut(df['A'], np.arange(0, 101, 10)))['B'].sum()

```




### 3. 按列聚合`groupby()`
1. 按照一列聚合
```python
dic1 = {'a': [1, 1, 1, 2, 2, 2], 'b': [2, 3, 4, 2, 3, 4], 'c': ['s', 's', 's', 's', 's', 's'], 'd': [6, 5, 4, 3, 2, 1]}
type(dic1)
df1 = pd.DataFrame(dic1)
df2 = df1.groupby(['b']) ## 把df1按照第二列聚合
df3 = df2.max()
```
> - 这时聚合的结果df2是一种特殊数据类型groupby类型
> - 如果要查看聚合结果, 必须要有聚合函数`max,min,sum,count,mean,median`等
> - df3是数据框

2. 按照某几列聚合
```python
dic1 = {'a': [1, 1, 1, 2, 2, 2], 'b': [2, 3, 4, 2, 3, 4], 'c': [1, 1, 2, 2, 3, 3], 'd': [6, 5, 4, 3, 2, 1]}
type(dic1)
df1 = pd.DataFrame(dic1)
df2 = df1.groupby(['a','c']) ## 把df1按照第二列聚合
df3 = df2.count()

## 这时候df3的索引是groupby的列值得组合张成的二维index
df3.index.tolist()
list(zip(df3.index.get_level_values(0),df3.index.get_level_values(1)))
index2one = [str(v[0])+'_'+str(v[1]) for v in zip(df3.index.get_level_values(0),df3.index.get_level_values(1))]

df3.columns.tolist()
```
> df3是数据框, 行名是(a,c)分别对应的值`[(1, 1), (1, 2), (2, 2), (2, 3)]`, 列名是`['b', 'd']`

3. 聚合后的数据有一个问题就是, groupby的列跑的行名上了, 为了使结果数据框的列和原始数据框的列一致
```python
dic1 = {'a': [1, 1, 1, 2, 2, 2], 'b': [2, 3, 4, 2, 3, 4], 'c': [1, 1, 2, 2, 3, 3], 'd': [6, 5, 4, 3, 2, 1]}
type(dic1)
df1 = pd.DataFrame(dic1)
df2 = df1.groupby(['a','c']) ## 把df1按照第二列聚合
df3 = df2.count()

# 第一种实现方式
df4 = df3.reset_index()

# 第二种实现方式
df3.reset_index(inplace=True)
```

4. 对不同的列使用不同的聚合函数
> eg.1
```
df = pd.DataFrame({'A': [1, 1, 2, 2], 'B': [1, 2, 3, 4], 'C': np.random.randn(4)})
df.groupby('A').agg({'B': ['min', 'max'], 'C': 'sum'})
```
结果为：
```
    B             C
  min max       sum
A
1   1   2  0.590716
2   3   4  0.704907
```
> eg.2 
直接重命名处理好的列
```
cate_sales_monthly = sku_sales_daily_modify.groupby(['item_third_cate_cd','YM'])['total_sales'].agg({'month_sales':np.sum})
```



# 3. 储存

### 3.1. 把数据框的内容存入excel
```python
## test for to_excel
import pandas as pd
import numpy as np
a = np.array(np.arange(12)).reshape(4,3)
b = {'a':[1,2,3,4], 'b':[5,6,7,8], 'c':[9,10,11,12], 'd':[13,14,15,16]}
df1 = pd.DataFrame(a)
df2 = pd.DataFrame(b)

writer = pd.ExcelWriter('output.xlsx')
df1.to_excel(writer,'Sheet1')
df2.to_excel(writer,'Sheet2')
# sheet1 and sheet2 can changed to any sheet names
writer.save()
```
### 3.2. 把数据框内容存入csv
```python
res[['filename','child','parent']].drop_duplicates().to_csv('table_relationship.csv',index=False)
```
> 存储的列和顺序为:'filename','child','parent'

> `drop_duplicates()`去除了重复的行

> `to_csv('table_relationship.csv',index=False)`在当前路径下存储为`csv`格式文件









---
---
---
---














#  数据框相关常用技巧
 

#### 1. 修正行索引`df.reset_index(inplace=True)`
> 在进行完行选择选出子集以后，可以修正行索引

> 很多方法在加上`inplace=True`以后，可以对前面的对象直接操作而不是返回一个操作后的对象

> `df.reset_index(dorp=FALSE)`会把之前的index单独弄成第一列

#### 2. 行转列
> `df.pivot(index='ProductDesc', columns='AttributeKey', values='AttributeValueKey')`

#### 3. 把数据框的某一列按照一个字典替换成字典中的值(excel的vlookup)
> `df[col] = df[col].map(attValDict)`

> `attValDict`中的key包含`df[col]`中的所有值

> `attValDict`中的value是要替换的值

> `attValDic`可以理解成一个一一映射（函数）

> 如果字典中的key不能覆盖`df[col]`的值域，则没有规则的key一律转化为NAN

```python
df111 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
map111 = {5:"f", 6:"g"}

df111['B'].map(map111)

'''
结果为：
    0    NaN
    1      f
    2      g

'''
```

#### 4. 生成连续的日期作为新的列
```python
import datetime as dt
import pandas as pd
MIN_TIME = '2017-2-2'
MAX_TIME = '2017-3-3'
df = pd.date_range(MIN_TIME, MAX_TIME).to_series().apply(lambda x: dt
.datetime.strftime(x, '%Y-%m-%d')).reset_index(drop=False, name='date')

```
> `pd.date_range(MIN_TIME, MAX_TIME)`张成一个时间序列, 开始时间为MIN_TIME, 结束时间为MAX_TIME

> `MIN_TIME`的形式既能是'2017-3-3'又能是'20170303'

> `.apply(lambda x: dt.datetime.strftime(x, '%Y-%m-%d'))`把日期统一格式

> `.reset_index(drop=False, name='date')`使得最后的数据由series变成dataframe

#### 5. 去掉某一列的极端值
```
import numpy as np
import scipy.stats
import pandas as pd
import copy
a = pd.Series(np.arange(100)+1)

b = copy.deepcopy(a)
b.loc[:] = scipy.stats.mstats.winsorize(a, limits = 0.05)

c = copy.deepcopy(b)
c.loc[:] = scipy.stats.mstats.winsorize(b, limits = [0.01, 0.1])
```
> - b: 把a中的1,2,3,4,5替换成6,6,6,6,6, 把a中的96,97,98,99,100替换成95,95,95,95,95

> - c: b中的6,6,6,6,6不变, 把b中的91,92,93,94,95,95,95,95,95,95都替换成90

> - [说明文档](https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.mstats.winsorize.html)

#### 6. 补全空缺值
一个dataframe的index与一个新的ndex匹配, 匹配上的就是原值, 匹配不上置零
```python
index = ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror']
df = pd.DataFrame({'http_status': [200,200,404,404,301], 'response_time': [0.04, 0.02, 0.07, 0.08, 1.0]}, index=index)

new_index= ['Safari', 'Iceweasel', 'Comodo Dragon', 'IE10', 'Chrome']
df1 = df.reindex(new_index, fill_value=0)


'''
结果为
>>> df
           http_status  response_time
Firefox            200           0.04
Chrome             200           0.02
Safari             404           0.07
IE10               404           0.08
Konqueror          301           1.00

>>> df1
               http_status  response_time
Safari                 404           0.07
Iceweasel                0           0.00
Comodo Dragon            0           0.00
IE10                   404           0.08
Chrome                 200           0.02
'''
```
> [说明文档](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.reindex.html)

#### 7. 指数移动平均

```python
import numpy as np
import pandas as pd
a = pd.Series(np.arange(100)+1)
b1 = pd.ewma(a, com=0.5)
b2 = pd.ewma(a, span=2)
b3 = pd.ewma(a, halflife=2)
```
> - `pd.ewma()`的作用对象是series或者dataframe
> - `com=0.5`是用质心的方式指定计算的范围(decay): alpha= 1/(1+com)
> - `span=1.5`是用span的方式确定decay: alpha= 2/(1+span)
> - `halflife=2`是用半衰期的方式确定decay: alpha= 1-exp(log(0.5)/halflife)
> - `com= (span-1)/2`
> [说明文档](http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.ewma.html)

#### 8. 把日期取为年月日
```python
imoprt pandas as pd
import datetime as dt
MIN_TIME = '20170202'
MAX_TIME = '20170303'
df = pd.date_range(MIN_TIME, MAX_TIME).to_series().apply(lambda x: dt.datetime.strftime(x, '%Y-%m-%d')).reset_index
(drop=False, name='Date')
df['DateTime'] = [dt.datetime.strptime(date, '%Y-%m-%d') for date in df['Date']]
df['Year'] = pd.DatetimeIndex(df['DateTime']).year
df['Month'] = pd.DatetimeIndex(df['DateTime']).month
df['Day'] = pd.DatetimeIndex(df['DateTime']).day
```

> pd.DatetimeIndex().year可以把一个时间向量中的年份取出来


#### 9. 差值(相邻值的平均值代替NAN)
```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(10)+1)
df.loc[3, 0] = np.nan
df.loc[7, 0] = np.nan
df[0].interpolate(inplace=True)
```
> 默认是线性差值, 取上下游相邻的两个值的算术平均

> [说明文档](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.interpolate.html)


#### 10. 建立组内序号的方法
```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.repeat([1,2,3],5))
df.rename(columns={0:'group'}, inplace=True)
df['index_in_group']= df.groupby(['group']).cumcount() + 1

'''
结果为: 
df
    group  index_in_group
0       1               1
1       1               2
2       1               3
3       1               4
4       1               5
5       2               1
6       2               2
7       2               3
8       2               4
9       2               5
10      3               1
11      3               2
12      3               3
13      3               4
14      3               5

'''
```

#### 11. 像使用join一样连接两张表
```python
import pandas as pd
c = pd.merge(a[['A','B']],b[[B'','C']], on = 'B')
```

#### 12. 拼接两个数据框
```python
import pandas as pd
df = pd.concat[df, df1, axis=0]
```
> - axis=0是按行拼接

> - axis=1是按列拼接

> - [说明文档](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html)




#### 14. 对数据框施用某种函数

###### 14.1. 每列分别使用某种函数: `apply()`
```python
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
f1 = lambda x: x.max() - x.min()
frame.apply(f1)
"""
结果为:
b    1.133201
d    1.965980
e    2.829781
"""
```
> `apply`既能作用于dataframe, 也能作用于series.


###### 14.2. 每个元素分别使用某种元素: `applymap()`
```python
## 接上面的frame
f2 = lambda x: '%.2f' % x
frame.applymap(f2)
"""
结果为:
            b      d      e
Utah    -0.03   1.08   1.28
Ohio     0.65   0.83  -1.55
Texas    0.51  -0.88   0.20
Oregon  -0.49  -0.48  -0.31
"""

```
> applymap只能作用于dataframe

###### 14.3 比较`map()`, `apply()`, `applymap()`
```python
## 对于f1这种对向量操作的函数
frame.apply(f1) ##可以正常运行
frame.map(f1) ##报错(由于map作用的类型)
frame.applymap(f1)  ##报错(由于函数f1作用域的类型)

frame['e'].apply(f1) ##报错(由于函数f1作用域的类型)
frame['e'].map(f1)  ##报错(由于函数f1作用域的类型)
frame['e'].applymap(f1)  ##报错(由于applymap作用的类型)

frame[['e']].apply(f1) ## 可以正常运行
frame[['e']].map(f1)  ## 报错(由于map作用的类型)
frame[['e']].applymap(f1)  ##报错(由于函数f1作用域的类型)




## 对于f2这种对标量操作的函数
frame.apply(f2) ##报错(由于函数f2作用域的类型)
frame.map(f2) ##报错(由于map作用的类型)
frame.applymap(f2)  ##可以运行

frame['e'].apply(f2) ## 可以正常运行
frame['e'].map(f2)  ## 可以正常运行
frame['e'].applymap(f2)  ## 报错(由于applymap作用的类型)

frame[['e']].apply(f2) ## 报错(由于函数f2作用域的类型)
frame[['e']].map(f2)  ##报错(由于map作用的类型)
frame[['e']].applymap(f2)  ## 可以正常运行

```
> 总结来看:
> 1. 只有当函数是对标量进行操作时, `map()`才能使用, 并且只能用于series上.

> 2. 只有当函数是对标量进行操作时, `applymap()`才能使用, 并且只能用于dataframe.

> 3. 当函数是对向量进行的操作时, `apply()`只能施用于dataframe上.
当函数是对标量进行的操作时, `apply()`只能施用于siries上.
