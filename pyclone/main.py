weight=int(input('Please input your weight'))
length=float(input('Please input your length'))
BMI=weight/(length*length)
print('Your BMI is')
if BMI >= 1:
    assert BMI < 1, 'that is not right'
else:

    print("{}".format(BMI))