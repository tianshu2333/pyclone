# "{}, {} and {}".format("first", "second", "third") 是用于替换没有名称的字符串的形式
#大括号内可以加数字，由于指定用后面第几个元素来替换前面模板内的内容，如
# >>> "{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to")
# 'to be or not to be'
# from math import pi
# "{name} is approximately {value:.2f}.".format(value=pi, name="pi")
# print("{pi!s}{pi!r}{pi!a}".format(pi="π"))

# print("The Middle by jimmpy Eat World".center(39))
# print("The Middle by jimmpy Eat World".center(39,"%"))

seq = ['asd', 'aqwesd', 'agdfsd', 'asgdfd', 'asdsa']
sep =  '+'
dir = '+'.join(seq)

print(dir)