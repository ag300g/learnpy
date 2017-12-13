lambda 定义了一个匿名函数

lambda 并不会带来程序运行效率的提高，只会使代码更简洁。

如果可以使用for...in...if来完成的，坚决不用lambda。

### 1.`lambda`是一种匿名函数，使用时并不必在使用`def UDF(): `
```python
# 直接定义函数g
g = lambda x:x*x

# 只需一行这个函数就写好了，可以直接调用
print(g(10))
# 的运行结果是：100　　　

# 这相当于通过以下方式定义了函数g
def g(x):
    return x+1
```
> lambda简化了函数定义的书写形式。使得代码更为简洁
> lambda也使得函数的定义方式更为直观，易理解。

### 2. `lambda`常常和和pyhton自带的三个全局函数配合使用

```python
foo = range(1,11)

print filter(lambda x: x % 3 == 0, foo)
# [3, 6, 9]

print map(lambda x: x * 2 + 10, foo)
# [12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

print reduce(lambda x, y: x + y, foo)
# 55
```

### 3. 上面的`filter`和`map`都是为了遍历，用`for..in..if语法`可以更简洁的实现
> 上面的`map(lambda x: x * 2 + 10, foo)`可以使用`[x * 2 + 10 for x in foo]`

> 上面的`filter(lambda x: x % 3 == 0, foo)`可以使用` [x for x in foo if x % 3 == 0]`


### 4. `lambda`可以结合`...if ... else ...`使用
```python
lower = (lambda x, y: x if x < y else y)
lower('bb', 'aa')
# 'aa'
```


### 5. `lambda`的作用域
典型的使用如下：lambda出现在def中，并且在上层函数调用时，嵌套的lambda能够获取到上层函数作用域中的变量名x的值。

```python
>>> def action(x):
    return (lambda y: x + y)
 
>>> act = action(99)

>>> act
<function action.<locals>.<lambda> at 0x0000014EF59F4C80>

>>> act(2)
101
```

### 6. 嵌套`lambda`
```python
>>> action = (lambda x:(lambda y: x + y))
>>> act = action(99)
>>> act(3)
102
>>> ((lambda x: (lambda y: x + y))(99))(4)
103
```

这里嵌套的lambda结构让函数在调用时创建了一个函数。嵌套的lambda代码都能够获取上层lambda函数中的变量x。这可以工作，但是这种代码让人相当费解。处于可读性的要求，通常来说，最好避免使用嵌套的lambda。