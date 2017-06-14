### lambda的使用(py27)
```python
# 返回一个数组中最大的元素
f = lambda a,b: a if (a > b) else b
reduce(f, [47,11,42,102,13])
```



```python
# 返回1到100个加和
reduce(lambda x, y: x+y, range(1,101))
```





### 关于循环的例子
```python
# 输出 2 到 100 间的质数
prime = []
for num in range(2,100):  # 迭代 2 到 100 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      prime.append(num)
print prime
```

```python
# 输出 2 到 100 间的质数
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " 是素数"
   i = i + 1
```

```python
# 打印空心等边三角形
rows = int(raw_input('输入行数：'))
for i in range(0, rows):
    for k in range(0, 2 * rows - 1):
        if (i != rows - 1) and (k == rows - i - 1 or k == rows + i - 1):
            print " * ",
        elif i == rows - 1:
            if k % 2 == 0:
                print " * ",
            else:
                print "   ",
        else:
            print "   ",
    print "\n"
```
### `pass`用法
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*- 

# 输出 Python 的每个字母
for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter

print "Good bye!"
```

### `list`用法
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

list01 = ['runoob', 786, 2.23, 'john', 70.2]
list02 = [123, 'john']

print list01
print list02

# 列表截取

print list01[0]
print list01[-1]
print list01[0:3]

# 列表重复

print list01 * 2

# 列表组合

print list01 + list02

# 获取列表长度

print len(list01)

# 删除列表元素

del list02[0]
print list02

# 元素是否存在于列表中

print 'john' in list02  # True

# 迭代

for i in list01:
    print i

# 比较两个列表的元素

print cmp(list01, list02)

# 列表最大/最小值

print max([0, 1, 2, 3, 4])
print min([0, 1])

# 将元组转换为列表

aTuple = (1,2,3,4)
list03 = list(aTuple)
print list03

# 在列表末尾添加新的元素

list03.append(5)
print list03

# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

list03.extend(list01)
print list03

# 统计某个元素在列表中出现的次数

print list03.count(1)

# 从列表中找出某个值第一个匹配项的索引位置

print list03.index('john')

# 将对象插入列表

list03.insert(0, 'hello')
print list03

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

print list03.pop(0)
print list03

# 移除列表中某个值的第一个匹配项

list03.remove(1)
print list03

# 反向列表中元素

list03.reverse()
print list03

# 对原列表进行排序

list03.sort()
print list03
```

### 全局变量与局部变量
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

globvar = 0

def set_globvar_to_one():
    global globvar    # 使用 global 声明全局变量
    globvar = 1

def print_globvar():
    print(globvar)     # 没有使用 global

set_globvar_to_one()
print  globvar        # 输出 1
print_globvar()       # 输出 1，函数内的 globvar 已经是全局变量
```

### 对象的创建

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
 
"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
```
以上代码的结果为:
```python
Name :  Zara ,Salary:  2000
Name :  Manni ,Salary:  5000
Total Employee 2
```


### 对象的内置类属性

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
 
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
```
代码结果为:
```python
Employee.__doc__: 所有员工的基类
Employee.__name__: Employee
Employee.__module__: __main__
Employee.__bases__: ()
Employee.__dict__: {'__module__': '__main__', 'displayCount': <function displayCount at 0x10a939c80>, 'empCount': 0, 'displayEmployee': <function displayEmployee at 0x10a93caa0>, '__doc__': '\xe6\x89\x80\xe6\x9c\x89\xe5\x91\x98\xe5\xb7\xa5\xe7\x9a\x84\xe5\x9f\xba\xe7\xb1\xbb', '__init__': <function __init__ at 0x10a939578>}
```

### 对象的回收
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "销毁"
 
pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3) # 打印对象的id
del pt1
del pt2
del pt3
```
代码结果为:
```python
3083401324 3083401324 3083401324
Point 销毁
```

### 字典作为备忘, 以减少程序运行时间
```python
known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1)+fibonacci(n-2)
    known[n] = res
    return res
```