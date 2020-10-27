import math
import cmath
import turtle
#关于整除和余数问题
a = 10 % 3
b = 10 % -3
c = -10 % 3
d = -10 % -3

#py内变量不能以数字开头
ex = math.floor(32.999)
print(ex)

ex2 = math.sqrt(1)
ex3 = cmath.sqrt(-1)
print(ex3)
#math模块是用于实现在实数间运算的，cmath是可以用于实现虚数计算
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
#字符串要避免转义有两种解决方案，一个是采用
# print(r'xxxxx')
# 另一个是
# print('''xxxxxx''')

ex4 = "\u00C6"
print(ex4)
ex5 = "\N{Cat}"
print(ex5)
#
# example1 = 'Because it is an exam'
# ex6 = example1[1]
# print(ex6)
# 切片中包含头但是不包含尾
