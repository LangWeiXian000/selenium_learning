
#创建一个My_class类,object是所有类的基类，所有类在创建时默认继承object
class My_class(object):
    def say_hello(self,name):
        return "hello, " + name

    def say_hi(self,name):
        return "hi, " + name
cl = My_class()
print(cl.say_hello('tom'))
print(cl.say_hi('hh'))
'''
object是所有类的基类，所有类在创建时默认继承object
类与函数的唯一区别是，方法的第一个参数必须要声明，一般习惯为’self‘，但在调用时并不需要为该参数设置数值
'''

class A:
    #A类的初始化方法
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    #调用这个方法时，默认执行初始化方法
    def add(self):
        return self.a + self.b
# count = A('4',5)
# print(count.add())
#B类继承A类，所以B类也拥有add()方法
class B(A):
    def sub(self,a,b):
        return a-b

print(B(10,6).add())#通过B类调用A类里的add()方法并打印
