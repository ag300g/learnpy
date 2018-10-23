## some examples


class Rctangle:
    def area(self):
        return self.length*self.width

r = Rctangle()
r.length = 10
r.width=5
r.area()


class Parent:
    def pprt(self):
        print(self)

class Child(Parent):
    def cprt(self):
        print(self)

c = Child()
c.cprt()
c.pprt()
p = Parent()
p.pprt()

class Person:
    grade=1
    def __init__(self):
        print(self.grade)

s = Person()

class Student(object):
    pass

t = Student("John",95.5)
t.__class__
t.__class__.__bases__



class Student():
    pass

t = Student()
t.__class__.__bases__


class X:
    pass

t = X()
t.__class__.__bases__



class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print "%s: %s" % (self.__name, self.__score)

t = Student("John",95.5)






class Desc:
    def __get__(self, ins, cls):
        print('self in Desc: %s ' % self )
        print(self, ins, cls)
class Test:
    x = Desc()
    def prt(self):
        print('self in Test: %s' % self)
t = Desc()
t1 = Test()
t.prt()
t.x





class Test:
    def ppr(self):
        print(self)
        print(self.__class__)

t = Test()
t.ppr()







class Cat:
    """定义了一个Cat类"""

    #初始化对象
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age

    #方法
    def eat(self):
        print("猫在吃鱼....")

    def drink(self):
        print("猫正在喝kele.....")

    def introduce(self):
        print("%s的年龄是:%s"%(self.name, self.age))


instance = Cat("Tom","2")
