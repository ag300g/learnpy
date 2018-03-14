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







