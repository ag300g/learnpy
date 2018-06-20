#### 隐式基类--`object`
1. 所有类都会继承`object`类

2. 延迟赋值
```python
class Rctangle:
    def area(self):
        return self.length*self.width
```

```python
>>> r = Rctangle()
>>> r.length = 10
>>> r.width=5
>>> r.area()
50
```
> 延迟初始化看似提供了某种灵活性, 但却给调用者带来了潜在的困惑, 因此要尽量避免这样的用法
