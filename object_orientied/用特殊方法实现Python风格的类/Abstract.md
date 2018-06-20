
#### 用特殊方法实现Python风格的类
1. 用特殊方法实现Python风格的类是对传统面向对象设计的一种延伸, 可以使python创建的类更具python风格
2. 任何一个类都应该与python语言其余的任何原生部分很好的结合
3. 这样一来, 不仅可以重用很多其他语言现有的功能和标准库, 而且编写的包和模块也将更容易维护和扩展

#### Python提供的特殊方案
1. 特性访问(attribute Access)
> e.g. `object.attribute`, 既可以来赋值, 也可以在del语句中执行删除操作
2. 可调用对象(Callables)
> e.g. `len(object)`
3. 集合(Collections)
> 提供了很多集合操作的功能
> e.g. `sequence[index]`, `mapping[key]`, `some_set|another_set`
4. 数字(Numbers)
> 提供了大量的数据运算符和比较运算符
5. 上下文(Context)
> 这类函数通常使用`with`语句来实现上下文的管理
6. 迭代器(Iterator)
> 可以使用这类方法定义迭代器, 然而我们通常不需考虑这方面的扩展, 因为生成器(Generator)已经提供了非常优雅的实现