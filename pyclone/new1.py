e = [["A",52,1.7],['B',75,1.6],["C",73,1.8]]
# give the origin data
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
    print("Sorry we cannot find this guy LOL")
