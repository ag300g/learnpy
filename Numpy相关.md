1. 创建一个从1到10的向量
```python
Z = np.arange(1,11)
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
