### 数据相关的常用库
1. NumPy库
> 多维数组，对多维数组元素基本的数学运算函数
2. pandas库
> 处理DataFrame对象，源自于R中的data.frame
3. matplotlib
> 最流行的绘制图表的库，与IPython配合，提供了非常好用的交互式绘图环境
4. IPython
> 是一个增强的Python Shell。主要用于交互式数据处理和利用matplotlib对数据进行可视化处理
5. SciPy
> 是一组专门解决科学计算中各种标准问题域的包的集合
（假设检验，矩阵分解，微分方程求解，稀疏矩阵等）
### 变量名
1. 由数字, 字母, 下划线组成, 但是不能以下划线开头, 区分大小写
> - 以单下划线开头 `_foo` 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 `from xxx import *` 而导入
> - 以双下划线开头的 `__foo` 代表类的私有成员
> - 以双下划线开头和结尾的 `__foo__` 代表 Python 里特殊方法专用的标识，如 `__init__()` 代表类的构造函数
2. python保留字(不能作用自定义类型)
> --- | --- | --- | --- | ---
> :---: | :---: | :---: | :---: | :---:
> and | exec | not | assert | finally
> or | break | for | pass | class
> from | print | continue | global | raise
> def | if | return | del | import
> try | elif | in | while | else
> is | with | except | lambda | yield

### 行和缩进
1. Python 的代码块使用**缩进**来控制类，函数以及其他逻辑判断
> 以下语句将报错
```python
if True:
    print "True"
else:
   print "False"
```
> `IndentationError: unexpected indent` 错误: 空格或者tab使用个数不一致
> `IndentationError: unindent does not match any outer indentation level`错误: 缩进方式不一致, 空格和tab混搭了

2. Python语句中一般以新行作为为语句的结束符。但是我们可以使用斜`\`将一行的语句分为多行显示
> 语句中包含 [], {} 或 () 括号就不需要使用多行连接符。

#### 注释
1. 使用`#`进行单行注释, 
2. 使用`"""`或者`'''`进行多行注释

### 打印
1. 流式打印
```python
a = "Hello"
b = "Python"

print "a + b 输出结果：", a + b 
print "a * 2 输出结果：", a * 2 
print "a[1] 输出结果：", a[1] 
print "a[1:4] 输出结果：", a[1:4] 
```
```
结果为： 
a + b 输出结果： HelloPython
a * 2 输出结果： HelloHello
a[1] 输出结果： e
a[1:4] 输出结果： ell

```
2. 格式打印
```python
print "My name is %s and weight is %d kg!" % ('Zara', 21) 
```
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
3. Python三引号
> python可以使用三个'''或者"""把一个带有复杂符号的代码原封不动的复制到某个变量上, 好处是不用使用**转义字符**
> 三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所见即所得的。

4. 函数辅助格式化打印
```python
"{1} {0} {1}".format("hello", "world")  # 设置指定位置
```
> 输出为: `'world hello world'`

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
 
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是可选的
```
> 输出为:
```
网站名：菜鸟教程, 地址 www.runoob.com
网站名：菜鸟教程, 地址 www.runoob.com
网站名：菜鸟教程, 地址 www.runoob.com
```
```python
print("{:.2f}".format(3.1415926))
```
> 输出为:
```
3.14
```

### 匿名函数
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;
 
# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )
print "相加后的值为 : ", sum( 20, 20 )
```

### 模块
1. 导入模块
> `import a`采用这种方式导入时在默认的路径下应该有一个`a.py`的文件, 并且要使用这个脚本中的函数`f1`要使用`a.f1()`

> `from a import *`采用这种方式导入时在默认的路径下应该有一个`a.py`的文件, 要使用这个脚本中函数`f1`只需使用`f1()`

> `from a import f1`采用这种方式, 不会导入整个模块, 只导入函数f1

2. 导入模块时的搜索路径
> 1. 当前目录

> 2. 如果不在当前目录，Python 则搜索在 shell 变量 `PYTHONPATH` 下的每个目录。

> 3. 如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。

3. `PYTHONPATH`变量设置
> `set PYTHONPATH=c:\python27\lib;` windows

> `set PYTHONPATH=/usr/local/lib/python` unix

### 文件读取
1. File 对象方法
> file对象提供了操作文件的一系列方法。

2. OS 对象方法
> 提供了处理文件及目录的一系列方法。

### 其他``````
1. py脚本首行加上: `#!/usr/bin/python`或者`#!/usr/bin/env python3`
> 通过命令行执行python代码时, 就不用使用`python 1.py`, 而可以直接执行`./1.py`

2. 首行加上: `# -*- coding: UTF-8 -*-`
> 可以使python支持中文输出

3. `isinstance(a,int)`
> 可以检验a是否是int的一个实例

4. 数值型和字符串型数据不能更改
> strings, tuples, numbers

5. 想要在函数内部给全局变量赋值, 必须在使用这个变量时用`global`声明这是一个全局变量
> - 如果一个全局变量是可以更改的数据类型, 实际上不用`global`声明也可以对他进行修改

> - 但是如果要给全局变量重新赋值, 则必须使用`global`字段声明他是全局变量

6. `structshape()`
> `structshape`函数见`scripts`文件夹
> 需要先`import`再使用:`from structshape import structshape`
> 查看一个类的类型和内容的基本信息
