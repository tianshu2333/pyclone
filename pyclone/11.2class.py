# list
# a = [0, 1, 2]
# print( a )
#
# # test 0
# a=5
# print('a is equal to {}'.format(a))
# # test1
# weight=int(input('Please input your weight'))
# length=int(input('Please input your length'))
# BMI=weight/(length*length)
# print('Your BMI is')
# if BMI >= 1:
#     assert BMI < 1, 'that is not right'
#     print(">>>><<<<")
# else:
#
#     print("{}".format(BMI))
# input在指定数字是必须指定变量类型，否则是作为字符串

# e = [["A",52,1.7],['B',75,1.6],["C",73,1.8]]
# print(e[1][1])
# print(e)
# e.append(27)
# print(e)
# name=input("Whose BMI do you want?")
# if  name==e[0][0]:
#     print(e[0][1]/(e[0][2]*e[0][2]))
# elif name==e[1][0]:
#     print(e[1][1] / (e[1][2] * e[1][2]))
# elif name==e[2][0]:
#     print(e[2][1] / (e[2][2] * e[2][2]))
# else:
#     print("cannot calculate")
# BMI calculate
# assert命令只能运行在if或elif之后，但是不能运行在else之后


# exercise2
e = [["A",52,1.7],['B',75,1.6],["C",73,1.8]]
# print(e[1][1])
# print(e)
# e.append(27)
# print(e)
# name = "C"
name=input("Whose BMI do you want?")
assert  name == "A" or name == "B" or name == "C","Sorry we cannot find this guy LOL"
if  name==e[0][0]:
    print(e[0][1]/(e[0][2]*e[0][2]))
    print('you are soo thin please eat more.')
elif name==e[1][0]:
    print(e[1][1] / (e[1][2] * e[1][2]))
    print('Your BMI is ok, keep it!')
elif name==e[2][0]:
    print(e[2][1] / (e[2][2] * e[2][2]))
    print('You are so heavy, please eat less and do more exercises.')
else:
    assert ("Sorry we cannot find this guy LOL")
# BMI calculate and suggestions