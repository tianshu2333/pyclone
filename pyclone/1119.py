# class MuffledCalculator:
#     muffled = False
#     def calc(self, expr):
#         try:
#             return eval(expr)
#         except ZeroDivisionError:
#             if self.muffled:
#                 print('Division by zero is illegal')
#             else:
#                 raise
# calculator = MuffledCalculator()
#
# print(calculator.calc('10/2'))
# print(calculator.calc('10/0'))
# __import__()
# __init___
# __iter

# class FooBar:
#     def __init__(self):
#         self.somevar = 42
#
# f = FooBar.somevar

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')
class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)
sb = SongBird()
sb.sing()
sb.eat()
sb.eat()