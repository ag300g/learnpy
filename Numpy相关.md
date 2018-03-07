1. 创建一个从1到10的向量
```python
Z = np.arange(1,11)
print(Z)

Z = 1+np.arange(10)
print(Z)
```
2. 倒序一个向量
```python
Z = np.arange(1,11)
print(Z[::-1])
```
3. 找到一个列表中的非零元素
```python
a = [1,2,0,0,10,0]
nz = np.nonzero(a)
ind = nz[0]
print(ind)
## 返回的结果是 0,1,4, 是a中非零元素的下标
nonzeroa = [a[i] for i in ind]
## 通过这种方式可以取得a中的非零元素
```
4. 初始化一个矩阵用以计算实验
```python
Z = np.random.random((10,10))  ## 10*10矩阵,每个元素都是标准正态分布中随机抽取的数
Z = np.ones((10,10))  ## 10*10矩阵, 每个元素都是1
Z = np.eye(10)  ## 10*10矩阵, 单位阵
Z = np.diag(1+np.arange(10))  ## 10*10矩阵, 对角元素为1到10
Z = np.zeros((10,10),dtype=int)  ## 10*10矩阵, 每个元素都是0
```

5. 以下几个判断的计算结果为:
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
