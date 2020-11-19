# def hello(name):
#     # 注意要缩进来明明函数
#     return '{} !'.format(name)
# print(hello('hello world' ))
#
# def fib(times):
#     result = [0, 1]
#     for i in range(times-2):
#         new = result[-2] + result[-1]
#         result.append(new)
#     return result
# print(fib(10))
# the fib
# 包含input选项在内，作为函数的参数进行输入
# 另外，不要忘记再定义函数之后，需要再后面输入：
# 返回的和定义的参数仅仅作为局部变量在这个函数中可以使用。
#
#
# def story(**kwds):
#     return 'Once upon a time, there was a ' \
#            '{job} called {name}.'.format_map(kwds)
# def power(x, y, *others):
#     if others:
#         print('Received redundant parameters:', others)
#     return pow(x, y)
# def interval(start, stop=None, step=1):
#     'Imitates range() for step > 0'
#     if stop is None: # 如果没有给参数stop指定值，
#        start, stop = 0, start # 就调整参数start和stop的值
#     result = []
#     i = start # 从start开始往上数
#     while i < stop: # 数到stop位置
#         result.append(i) # 将当前数的数附加到result末尾
#         i += step # 增加到当前数和step（> 0）之和
#     return result
#
#
# print((5,) * 2)

class Person:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def greet(self):
        print("Hello, world! I'm {}.".format(self.name))
# 类的例子
foo = Person()
bar = Person()
foo.set_name(('Luke skywalker'))
bar.set_name(('Anakin skywalker'))
foo.greet()
bar.greet()
print(foo.name)