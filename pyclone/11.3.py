# 对于逻辑判断，is 和 == 表示不一样的意思
# is 表示指向同一个东西（列表etc），两个对象指向的是一个东西。而 == 表示两个变量的值是相等的，可以认为is的优先级高于==

# x = 1
# while x <= 100:
#     print(x)
#     x += 1

# name = ''
# while not name:
#     name = input('Please enter your name: ')
# print('Hello, {}!'.format(name))

# ABS = ['this', 'is', 'an', 'ex', 'parrot']
# for word in ABS:
#     print(word)
#
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number in numbers:
#     print(number)
# 对于word和number，都是指代一类的事物，即使不定义也可以使用。


# d = {'x': 1, 'y': 2, 'z': 3}
# print(d.items())
#
# names = ['anne', 'beth', 'george', 'damon']
# ages = [12, 45, 32, 102]
# for i in range(len(names)):
#     print(names[i], 'is', ages[i], 'years old')
#     # 自动执行i++
#
# print(list(zip(range(5),range(10))))

# word = 'dummy'
# while word:
# word = input('Please enter a word: ')
# # 使用这个单词做些事情：
# print('The word was', word)

# while True:
#     word = input('Please enter a word: ')
#     if not word:
#         break
#         # 使用这个单词做些事情：
#     print('The word was', word)

# print([x * x for x in range(10)])

# girls = ['alice', 'bernice', 'clarice']
# boys = ['chris', 'arnold', 'bob']
# print([b+'+'+g for b in boys for g in girls if b[0] == g[0]])

from math import sqrt
scope = {}
exec('sqrt = 1', scope)
print(sqrt(4))
 
print(scope['sqrt'])
print('scope')
print()