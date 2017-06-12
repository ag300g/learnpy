### 元组类及相关方法
1. 创建一个元组
```python
t1 = ('a','b','c','d')
t2 = 'a','b','c','d'
t3 = 'a'
t4 = 'a',
t5 = ('a')
type(t1)  #是一个元组
type(t2)  #是一个元组
type(t3)  #是一个字符串
type(t4)  #是一个元组
type(t5)  #是一个字符串
t6 = tuple()
t7 = tuple('Michael')
```
2. 元组交换值
> `a, b = b, a`

3. `divmod(a,b)`
> 返回一个元组,第一个数字是a/b的商, 第二个数是a/b的余数

4. `zip()`
> 返回一个元组列表, 可以把两个列表或者两个元组一一对应起来(长的丢弃)

5. `enumerate()`
> 返回一个字符串或者列表的所有元素及下表对应的元组

6. 字典类中的`item()`方法, 返回一个与字典对应的元组
> 元组类中的`dict()`方法, 返回一个与元组对应的字典

7. 元组可以作为字典中的键