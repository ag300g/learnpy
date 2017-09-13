## 浅拷贝与深拷贝
Python中的对象之间赋值时是按引用传递的，如果需要拷贝对象，需要使用标准库中的copy模块。

1、copy.copy 浅拷贝 
> 只拷贝父对象，不会拷贝对象的内部的子对象。

2、copy.deepcopy 深拷贝
> 拷贝对象及其子对象
```python
import copy
a = [1,2,3,4,['a','b']]  #原始对象

b = a  #赋值，传对象的引用

c = copy.copy(a)

d = copy.deepcopy(a)

a.append(5)
a[4].append('c')
```
结果为：
```
>>> print 'a=',a
a= [1, 2, 3, 4, ['a', 'b', 'c'], 5]
>>> print 'b=',b
b= [1, 2, 3, 4, ['a', 'b', 'c'], 5]
>>> print 'c=',c
c= [1, 2, 3, 4, ['a', 'b', 'c']]
>>> print 'd=',d
d= [1, 2, 3, 4, ['a', 'b']]
```