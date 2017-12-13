### 1.`lambda`是一种匿名函数，使用时并不必在使用`def UDF(): `
```python
# 直接定义函数g
g = lambda x:x*x

# 只需一行这个函数就写好了，可以直接调用
print(g(10))
# 的运行结果是：100　　　
```
Python lambda实在是做的弱到不行……不能缩进（一个lambda函数只能写在一行），只能用if…else…，只能写一条语句等等。
