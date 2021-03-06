### 1. 创建一个从1到10的向量
```python
Z = np.arange(1,11)
print(Z)

Z = 1+np.arange(10)
print(Z)
```
### 2. 倒序一个向量
```python
Z = np.arange(1,11)
print(Z[::-1])
```
### 3. 找到一个列表中的非零元素
```python
"""
第一种方法, 使用列表去找
"""
a = [1,2,0,0,10,0]
nz = np.nonzero(a)
ind = nz[0]
print(ind)
## 返回的结果是 0,1,4, 是a中非零元素的下标
nonzeroa = [a[i] for i in ind]
## 通过这种方式可以取得a中的非零元素


"""
第二种方法, 使用np.array的性质
"""
a = [1,2,0,0,10,0]
arraya = np.array(a)

nz = np.arange(len(a))[arraya != 0]
nonzeroa = arraya[arraya != 0]
```
### 4. 初始化一个矩阵用以计算实验
```python
Z = np.random.random((10,10))  ## 10*10矩阵,每个元素都是标准正态分布中随机抽取的数
Z = np.ones((10,10))  ## 10*10矩阵, 每个元素都是1
Z = np.eye(10)  ## 10*10矩阵, 单位阵
Z = np.diag(1+np.arange(10))  ## 10*10矩阵, 对角元素为1到10
Z = np.zeros((10,10),dtype=int)  ## 10*10矩阵, 每个元素都是0
Z = np.random.randint(0,3,(3,10)) ## 3*10矩阵, 每个元素都是[0,3)之间的随机整数

Z = (1+np.arange(100)).reshape(10,10)  ## 10*10矩阵, 按照行分别自增1

```

### 5. 以下几个判断的计算结果为:
```python
0 * np.nan
##Out[51]: nan

np.nan == np.nan
##Out[52]: False

np.inf > np.nan
##Out[53]: False

np.nan - np.nan
##Out[54]: nan

0.3 == 3 * 0.1
##Out[55]: False

```

### 6. 归一化一个矩阵
```python
Z = np.random.random((5,5))
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)
```

### 7. 矩阵计算
```python

## 元素级四则运算
Z = np.arange(9).reshape(3,3)
print(Z+1)
print(Z-1)
print(Z*10)
print(Z/10)
print(Z**2) # 计算每个元素的平方值, 并返回


## 矩阵相乘
Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)

## 矩阵相加或者相减
np.zeros((5,3)) + np.ones((5,3))
np.zeros((5,3)) - np.ones((5,3))

## 每行分别相加减
np.zeros((5,3)) + np.ones((1,3))  # 后面的行数只能是5或者1
np.zeros((5,3)) - np.ones((1,3))  # 后面的行数只能是5或者1

## 每列分别相加减
np.zeros((5,3)) + np.ones((5,1))  # 后面的行数只能是3或者1
np.zeros((5,3)) - np.ones((5,1))  # 后面的行数只能是3或者1


np.zeros((5,3)) + np.arange(3) # 不会报错, 会把np.arange(3)默认是行向量进行计算
np.zeros((5,3)) + np.arange(5)  # 会报错, np.arange(5)默认是行向量, 前面的矩阵的列数不符

```
> - `np.arange(5)`没有行列信息, 进行矩阵计算时默认是一个 **行向量**
> - `np.arange(5)`在进行矩阵计算时等价于`np.arange(5).reshape(1,5)`, 但事实上并不是一个矩阵, 比如`np.arange(5).transpose()`无效, 仍然等价于`np.arange(5)`
> - `np.arange(5).reshape(1,5).transpose()`等价于`np.arange(5).reshape(5,1)`, 反之亦然



### 8. 四舍五入
```python
Z = np.random.uniform(-10,10,10)
## 向下取整
print (Z - Z%1)
print (np.floor(Z))

## 截断
print (np.trunc(Z))
print (Z.astype(int))

## 向上取整
print (np.ceil(Z)-1)

## 四舍五入
print (np.round(z))  ## 在有负数的时候会报错
print (np.trunc(Z + np.copysign(0.5, Z)))
```


### 9. 在0到1之间等距离生成10个点, 不包括0和1
```python
Z = np.linspace(0,1,11,endpoint=False)[1:]
print(Z)
```

### 10. 找到向量中最小的元素的下标
```python
## 简便方法
Z = np.random.uniform(0,10,100)
max_index = Z.argmax() # 最大值的下标
Z[max_index] # 最大值

## 复杂方法
Z = np.random.uniform(0,10,100)
Z.max() # 取得向量中最大的元素的值
np.arange(len(Z))[Z == Z.max()]  # 取得向量中最大元素的下标
Z[Z == Z.max()]  # 通过TRUE,FALSE的序列取得最大值
Z[(np.arange(len(Z)))[Z == Z.max()]]  # 通过下标取得最大值

```


### 11. 外加和外减
```python
X = np.arange(2)
Y = 10+np.arange(3)
C = np.subtract.outer(X, Y)  ## C实际上是一个2*3的矩阵, 其中c_ij对应的是x_i-y_j
```


### 12. 矩阵的一些特征
```python
from numpy import linalg as LA
a = np.arange(9) - 4
b = a.reshape((3, 3))
c = np.diag([1,2,3])

print(LA.det(b)) # 计算矩阵b的行列式
print(LA.norm(b)) # 计算矩阵b的范数
print(LA.inv(c)) # 计算矩阵c的逆矩阵
print(LA.eig(c)[0]) # 计算矩阵c的特征值
print(LA.eig(c)[1]) # 计算矩阵c的特征值对应的特征向量

## SVD分解
a = np.random.randn(9, 6)
U, s, V = np.linalg.svd(a, full_matrices=True) # 是TRUE时,U是9*9, V是6*6
S = np.zeros((9, 6))
S[:6, :6] = np.diag(s)
np.allclose(a, np.dot(U, np.dot(S, V)))

U, s, V = np.linalg.svd(a, full_matrices=False) # 是False时, U是9*6, V是6*6
U.shape, s.shape, V.shape
S = np.diag(s)
np.allclose(a, np.dot(U, np.dot(S, V)))

### 计算矩阵的秩
Z = np.random.uniform(0,1,(10,10))
U, S, V = np.linalg.svd(Z) # Singular Value Decomposition, 默认full_matrices=True
rank = np.sum(S > 1e-10) # 找到那些不为零的S的个数即为原矩阵的秩
```
> - `LA.norm(b,ord=None)` 可以指定要计算的范数类型, 默认是None

| ord   | norm for matrices            | norm for vectors           |
| ----- | ---------------------------- | -------------------------- |
| None  | Frobenius norm               | 2-norm                     |
| ‘fro’ | Frobenius norm               | –                          |
| ‘nuc’ | nuclear norm                 | –                          |
| inf   | max(sum(abs(x), axis=1))     | max(abs(x))                |
| -inf  | min(sum(abs(x), axis=1))     | min(abs(x))                |
| 0     | –                            | sum(x != 0)                |
| 1     | max(sum(abs(x), axis=0))     | as below                   |
| -1    | min(sum(abs(x), axis=0))     | as below                   |
| 2     | 2-norm (largest sing. value) | as below                   |
| -2    | smallest singular value      | as below                   |
| other | –                            | sum(abs(x)**ord)**(1./ord) |


### 13. 向量元素类型转换
```python
x = np.array([1, 2, 2.5])
x.astype(int)

Z = np.arange(10, dtype=np.int32)
Y = Z.astype(np.float32)
```


### 14. 行和 & 列和
```python
X = np.random.rand(5, 10) # 生成一个5*10列的矩阵

## 行和,行平均
Y = X.mean(axis=1, keepdims=True) # 每行求均值, 并且保留维度特征, 形成一个5*1的矩阵
Y = X.sum(axis=1, keepdims=False) # 每行求和, 丢弃维度特征, 形成一个长度为5的向量

## 列和,列平均
X = np.random.rand(5, 10) # 生成一个5*10列的矩阵
Y = X.mean(axis=0, keepdims=True) # 每列求均值, 并且保留维度特征, 形成一个1*10的矩阵
Y = X.sum(axis=0, keepdims=False) # 每列求和, 丢弃维度特征, 形成一个长度为10的向量

```
> 默认`keepdims=False`


### 15. 按照某列从小到大的顺序给一个矩阵的行重新排序
```python
Z = np.random.randint(0,10,(3,3))
print(Z)
print(Z[Z[:,1].argsort()])  # Z[:,1].argsort()返回Z的第2列从小到大排序后, 各个名次对应的行名
```


### 16. 统计一个非负整数向量的各个数字出现的个数
```python
I = np.random.randint(0,10,20)  # 生成[0,10)之间的随机整数组成的长度为20的向量
W = np.ones(20,dtype=int)
Y = np.bincount(I, minlength=10)  # 按照从0开始的顺序统计每个数字=出现的次数
Y_hat = np.bincount(I, weight=W)  # 每个数字按照对应的W中的wweight加权统计
```
> `minlength=10`意味着输出的Y最多只有10个数字, 默认值是`minlength=0`

> 如果I中最大的数字是5, 则`minlength=0,1,2,3,4,5,6`都可以输出从0到5(共6位)的统计结果

> 如果I中最大的数字是5, 而`minlength=7`都可以输出从0到6(共7位)的统计结果

> 上述代码中 Y 和 Y_hat 结果一致


### 17. 加权平均
```python
D = np.random.uniform(0,1,100)
S = np.random.randint(0,10,100)
D_sums = np.bincount(S, weights=D)
D_counts = np.bincount(S)
D_means = D_sums / D_counts
```

### 18. 索引和切片
```python
"""
切片
"""
arr = np.arange(12).reshape((3, 4))
print 'array is:'
print arr

# 取第一维的索引 1 到索引 2 之间的元素，也就是第二行
# 取第二维的索引 1 到索引 3 之间的元素，也就是第二列和第三列
slice_one = arr[1:2, 1:3]
print 'first slice is:'
print slice_one

# 取第一维的全部
# 按步长为 2 取第二维的索引 0 到末尾 之间的元素，也就是第一列和第三列
slice_two = arr[:, ::2]
print 'second slice is:'
print slice_two

>> array is:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
>> first slice is:
[[5 6]]
>> second slice is:
[[ 0  2]
 [ 4  6]
 [ 8 10]]
 
 
 """
 索引
 """
 # numpy类型的多位数组, 只需要用一个用一个中括号, 里面写好对应维度的下标即可. e.g. 要取二维数组arr的第2行第2列的那个元素: arr[1, 1]
 arr = np.array([
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [3, 6, 9, 12],
    [4, 8, 12, 16]
])
# 取下标[0,3]和[2,1]组成一个向量
print arr[[0, 2], [3, 1]]
>> [4 6]

# 取第0行和第2行的所有元素
print arr[[0, 2],:]
print arr[[0, 2]]

>> [[ 1  2  3  4]
 [ 3  6  9 12]]
>> [[ 1  2  3  4]
 [ 3  6  9 12]]


# 如果是python自带的list型数组,就要把每个维度分别用中括号括起来来引用
arr = [
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [3, 6, 9, 12],
    [4, 8, 12, 16]
]
print '第二行第二列的值:', arr[1][1]
try:
    print '第二行第二列的值(尝试用 Numpy 的方式获取):', arr[1, 1]
except Exception as e:
    print str(e)
    
>> 第二行第二列的值: 4
>> 第二行第二列的值(尝试用 Numpy 的方式获取): list indices must be integers, not tuple

```
> 在取切片数据时, 每一个维度都有三个参数可以传入, 中间以`:`间隔

> 不同的维度的参数使用`,`间隔

> `arr[i:j:k]`首先是假设arr是一个一维数组, 切片信息从下标`i`开始, 到下标`j`结束, 中间每隔`k`个就取出


### 19. 把数组A按照某种模式重复形成数组B
```python

# 把一个标量重复n次, 张成一个向量
np.repeat(3, 4)  
>> array([3, 3, 3, 3])


# 把一个向量重复n次, 张成一个长向量向量
np.repeat(np.arange(2), 4)  
np.repeat([0,1], 4) # 两行代码结果一致

>> array([3, 3, 3, 3])
>> array([3, 3, 3, 3])


# 把一个矩阵按照规定列或者行重复规定的次数, 张成一个更大的矩阵

#1#
x = np.array([[1,2],[3,4]])
np.repeat(x, 2)  # 如果不规定axis, 就会把x按向量处理
>> array([1, 1, 2, 2, 3, 3, 4, 4])
#2#
np.repeat(x, 3, axis=1) # 行数固定, 列数扩张, 每列重复3次
>> array([[1, 1, 1, 2, 2, 2],
       [3, 3, 3, 4, 4, 4]])
#3#
np.repeat(x, [1, 2], axis=0) # 列数固定, 行数扩张, 第0行重复1次, 第1行重复2次
>> array([[1, 2],
       [3, 4],
       [3, 4]])
```

### 20. 累加
```python
#1#
# 如果不指定行列, 就把矩阵当成向量处理
a = np.array([[1,2,3], [4,5,6]])
print(a)
>> array([[1, 2, 3],
       [4, 5, 6]])

print(np.cumsum(a))
>> array([ 1,  3,  6, 10, 15, 21])

print(np.cumsum(a, dtype=float))     # specifies type of output value(s)
>> array([  1.,   3.,   6.,  10.,  15.,  21.])

#2#
# 如果指定了行列, 就把在行或者列上进行累加
np.cumsum(a,axis=0)      # sum over rows for each of the 3 columns
>> array([[1, 2, 3],
       [5, 7, 9]])
np.cumsum(a,axis=1)      # sum over columns for each of the 2 rows
>> array([[ 1,  3,  6],
       [ 4,  9, 15]])
```


### 21. 计算一个向量的移动平均值
```python
def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
Z = np.arange(20)
print(moving_average(Z, n=3))
```
> `ret[:-n]`是去掉尾部n个数据

> `ret[n:]`是去掉头部n个数据


### 22. 逻辑向量的求反,普通向量取相反的符号
```python
Z = np.random.randint(0,2,100)
np.logical_not(Z, out=Z)

Z = np.random.uniform(-1.0,1.0,100)
np.negative(Z, out=Z)
```

### 23. 取一个array中最大的n个数
```python
Z = np.arange(10000)
np.random.shuffle(Z)
n = 5

# Slow
print (Z[np.argsort(Z)[-n:]]) # np.argsort(Z)按照从小到大的顺序Z中每个顺序对应的元素的下标是多少

# Fast
print (Z[np.argpartition(-Z,n)[:n]])
```
> `Z[np.argsort(Z)[i]] = np.sort(Z)[i]` 

### 24. 取一个array中>10的元素的下标
```python
x = np.arange(9.).reshape(3, 3)
np.where( x > 5 )
>>> (array([2, 2, 2]), array([0, 1, 2]))

x[np.where( x > 3.0 )]               # Note: result is 1D.
>>> array([ 4.,  5.,  6.,  7.,  8.])

np.where(x < 5, x, -1)               # Note: broadcasting.
>>> array([[ 0.,  1.,  2.],
       [ 3.,  4., -1.],
       [-1., -1., -1.]])
       
goodvalues = [3, 4, 7]
ix = np.isin(x, goodvalues)
ix
>>> array([[False, False, False],
       [ True,  True, False],
       [False,  True, False]], dtype=bool)

np.where(ix)
>>> (array([1, 1, 2]), array([0, 1, 1]))
```
> 返回的是下标信息, 如果是矩阵, 就返回两个数组, 分别对应两个维度的下标信息

### 25. 把两个矩阵拼接起来: np.concatenate
- 按行拼接
```
>>> a = np.array([[1, 2], [3, 4]])
>>> b = np.array([[5, 6]])
>>> np.concatenate((a, b), axis=0)
array([[1, 2],
       [3, 4],
       [5, 6]])
```
- 按列拼接
```
>>> np.concatenate((a, b.T), axis=1)
array([[1, 2, 5],
       [3, 4, 6]])
```
