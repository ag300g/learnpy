### join用法示例
> 用来连接字符串, 把一个`list`连接成一个`string`

```python
li = ['my','name','is','bob']
' '.join(li)
## 运行结果为: 'my name is bob'

'_'.join(li)
## 运行结果为: 'my_name_is_bob'

s = ['my','name','is','bob']
''.join(s)
## 运行结果为: 'mynameisbob'

'..'.join(s)
## 运行结果为: 'my..name..is..bob'
```

### split用法示例
> 用来拆分字符串, 把一个`string`拆分成`list`

```python
b = 'my..name..is..bob'
b.split()
## 运行结果为：['my..name..is..bob']

>>> b.split("..")
## 运行结果为：['my', 'name', 'is', 'bob']

>>> b.split("..",0)
## 运行结果为：['my..name..is..bob']

>>> b.split("..",1)
## 运行结果为：['my', 'name..is..bob']

>>> b.split("..",2)
## 运行结果为：['my', 'name', 'is..bob']

>>> b.split("..",-1)
## 运行结果为：['my', 'name', 'is', 'bob']
```
> `b.split("..",-1)`等价于`b.split("..")`