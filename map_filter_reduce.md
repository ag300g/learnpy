
# Map，Filter 和 Reduce
Map，Filter 和 Reduce 三个函数能为函数式编程提供便利。我们会通过实例一个一个讨论并理解它们。


## ```map```

**用法规范**: `map(function, sequence)`
> - `map`顾名思义, 会将一个函数'映射'到一个输入列表的所有元素上 
> - 即对`sequence`中的`item`依次执行`function(item)`，并将执行结果组成一个list返回

一些简短的例子:
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

实际上, 我们使用`map`是用一种简单而漂亮得多的方式来替代以下这种循环
> 这时如果有匿名函数`lambda`的配合, 连上面例子中的函数定义也可以省略
```python
## 每个元素都进行三次方的操作的朴素的实现方式
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**3)

## 使用map和lambda配合更简洁的实现方式
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**3, items))
```

更灵活的是, 还能通过`lambda`函数, 把一个函数list作为输入.

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
> 顾名思义，`filter`过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，**符合要求**即函数映射到该元素时返回值为True.
> 即对`sequence`中的`item`依次执行`function(item)`，将执行结果为`True`的`item`组成一个`List/String/Tuple`（取决于sequence的类型）返回

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
