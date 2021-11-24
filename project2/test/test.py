import sys
# '''
# 跨目录调用文件
# 首先看calcuator.py文件，python会根据这个目录的列表，由上到下依次寻找名为calcuator的目录或文件，显然project2这个目录下没有，所以无法直接调用
#
# calcuator.py的绝对路径是：F:\\pythonProject_selenium_test\\project2\\test
# 如何查看绝对路径：print（sys.path）
#
# 找到绝对路径后，将绝对路径添加到系统的path中即可
# '''
sys.path.append("F:\\pythonProject_selenium_test\\project2\\test")
from project1.calcuator import add
#
# print(add(2,3))
'''
解决了跨目录调用文件，但是实际应用中，你的代码需要提交到Git，其他人也需要拉取代码并执行，
这种情况下你无法保证其他人的项目路径跟你的一样，所以我们应该避免在项目中写绝对路径
'''
#优化代码如下
import sys
from os.path import dirname,abspath
project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path + "\\module")
from project2.module.module import add
# from project2.module.module import add
'''
__file__用于获取文件所在的路径，调用os.path下面的abspath(__file__)可以得到文件的绝对路径
dirname()函数用于获取上级目录，所以当两个dirname()函数嵌套使用时，得到的目录是：F:\\pythonProject_selenium_test\\project2
最后将这个路径与“\\module”目录拼接，可以找到module文件
'''

# from project1.calcuator import add
'''
if __name__ == '__main__':表示当模块被直接运行时，下面的代码块将被运行；
当代码块被其他程序文件调用时，下面的代码块将不被运行
'''
if __name__ == '__main__':
    b = add(5,3)
    print(b)