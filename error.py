# open("abc.txt",'r')
'''
报错信息为：FileNotFoundError: [Errno 2] No such file or directory: 'abc.txt'
'''

#如何捕捉异常
try:
    open("abc.txt","r")
except FileNotFoundError:
    print("请检查该文件是否存在")
try:
    a = "test"
    print(a)
except NameError:
    print("变量a找不到！")
'''
python2.5之前，所有的异常类都继承自Exception
python2.5之后，所有的异常类都有了新的基类BaseException,Exception同样也继承BaseException
所以可以直接用BaseException来接收所有类型的异常
'''
#有异常时返回异常信息
try:
    open("abc.txt","r")
    # print("cs")
except BaseException as msg:
    print(msg)
else:
    print("没有异常时执行！")

#不管有无异常都执行
try:
    a = "异常测试："
    print(a)
except BaseException as msg:
    print(msg)
finally:
    print("不管是否异常，都执行。")

#抛出异常 关键字用 raise
def say_hello(name):
    if name is None:
        raise BaseException("'name' cannot be empty")
    else:
        print("hello, " + str.format(name))
    return name


if __name__ == '__main__':
    test = say_hello('hh')
