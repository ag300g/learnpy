
# Map，Filter 和 Reduce
Map，Filter 和 Reduce 三个函数能为函数式编程提供便利。我们会通过实例一个一个讨论并理解它们。


## ```map```

**用法规范**: `map(function, sequence)`
> - `map`顾名思义, 会将一个函数'映射'到一个输入列表的所有元素上 
> - 即对`sequence`中的`item`依次执行`function(item)`，并将执行结果组成一个list返回

两个简短的例子:
```python
def cube(x): return x*x*x
map(cube, range(1, 11))
## 结果为：[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


def cube(x) : return x + x
map(cube , "abcde")
## 结果为：['aa', 'bb', 'cc', 'dd', 'ee']

## 另外map也支持多个sequence，这就要求function也支持相应数量的参数输入：
def add(x, y): return x+y
map(add, range(8), range(8))
## 结果为：[0, 2, 4, 6, 8, 10, 12, 14]
```

```python
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
```

`Map`可以让我们用一种简单而漂亮得多的方式来实现。就是这样：

```python
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```
大多数时候，我们使用匿名函数(lambdas)来配合`map`, 所以我在上面也是这么做的。
 不仅用于一列表的输入， 我们甚至可以用于一列表的函数！

```python
def multiply(x):
        return (x*x)
def add(x):
        return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = map(lambda x: x(i), funcs)
    print(list(value))
    # 译者注：上面print时，加了list转换，是为了python2/3的兼容性
    #        在python2中map直接返回列表，但在python3中返回迭代器
    #        因此为了兼容python3, 需要list转换一下

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
```




## ```filter```
**用法规范**: `filter(function, sequence)`
> 
> 即对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）返回

两个简短的例子：
```python
def f(x): return x % 2 != 0 and x % 3 != 0
filter(f, range(2, 25))
## 结果为：[5, 7, 11, 13, 17, 19, 23]

def f(x): return x != 'a'
filter(f, "abcdef")
## 结果为：'bcdef'
```

```python
number_list = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, number_list)
print(list(less_than_zero))  
# 译者注：上面print时，加了list转换，是为了python2/3的兼容性
#        在python2中filter直接返回列表，但在python3中返回迭代器
#        因此为了兼容python3, 需要list转换一下

# Output: [-5, -4, -3, -2, -1]
```

- `filter`类似于一个`for`循环，但它是一个内置函数，并且更快。
- 注意：如果`map`和`filter`对你来说看起来并不优雅的话，那么你可以看看另外一章：列表/字典/元组推导式。
> 译者注：大部分情况下推导式的可读性更好





## ```Reduce```

当需要对一个列表进行一些计算并返回结果时，`Reduce` 是个非常有用的函数。举个例子，当你需要计算一个整数列表的乘积时。

通常在 python 中你可能会使用基本的 for 循环来完成这个任务。

现在我们来试试 reduce：

```
from functools import reduce
product = reduce( (lambda x, y: x * y), [1, 2, 3, 4] )

# Output: 24
```
