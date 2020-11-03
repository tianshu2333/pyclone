# 创建字典，用于寻找对应的名称指代的值

# phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# items = [('name', 'Gumby'), ('age', 42)]
# d = dict(items)
# 使用dict可以以另一种方式来创建字典
# 前面的键为名字，后面的值为这个名字指代的对象

# 通过字典中的键来指出对应的值
phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'}
print("Cecil's phone number is {Cecil}.".format_map(phonebook))

# 当两个变量指向同样的字典时，通过一个变量对字典进行操作，则两个变量的值都会发生改变
# >>> x = {}
# >>> y = x
# >>> x['key'] = 'value'
# >>> y
# {'key': 'value'}
# >>> x = {}
# >>> x = {}
# {'key': 'value'}
# 和
# >>> x = {}
# >>> y = x
# >>> x['key'] = 'value'
# >>> y
# {'key': 'value'}
# >>> x.clear()
# >>> y
# {}
# b = ['asda', 'band', 'caonima']
# x = 1, b, 3
# b[1] = 'biasd'
# print(x[1])
# print(b)

x={}
y = x
x['key'] = 'value'
x = {}
print(x)
print
{}.fromkeys()