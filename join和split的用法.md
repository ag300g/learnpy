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

### 随机
1. 打乱顺序
```python
import random
lll = list(range(20))
random.shuffle(lll)
```

2. 从一个集合中随机抽出n个
```python
import random
### 从0~99中随机抽出10个数(无放回)
lll = random.sample(range(100),10)

### 从0~99中随机抽出10个数(有放回)
lll = random.choices(range(100),k=10)
```

3. 从某个分布中随机取数
```python
### 从一个均匀分布中取出n个数
lll = random.uniform(10, 20) # 均匀分布为 10<=n<=20

### 从[0,1]均匀分布中随机取一个数
lll = random.random()

### 从一个标准正态分布中取出n个数
lll = random.gauss(0,1)

```
