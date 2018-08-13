#### 1. `continue`可以避免使代码产生过多分支层级
> 未见得是好事
```
for x, y in zip(a, b):
  if x > y:
    z = calculate_z(x, y)
    if y-z < x:
      y = min(y, z)
      if x ** 2 - y ** 2 > 0:
        lots()
        of()
        codes()
        here()
```
可以使用`continue`改写为
```
for x, y in zip(a, b)
  if x <= y:
    continue
  z = calculate_z(x, y)
  if y-z < x:
    continue
  y = min(y, z)
  if x ** 2 - y ** 2 > 0:
    continue
  lots()
  of()
  codes()
  here()
  
```
