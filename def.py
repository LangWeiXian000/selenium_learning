#定义一个add函数
def add(a=1,b=4):
    return a + b
#调用函数add()
# c = add(3,5)
# print(c)
c = add()
c1 = add(5,7)
print(c)
print(c1)
'''
如果调用时不传参数，那么创建的函数add()会使用默认的参数进行计算，否则计算参数的值
'''