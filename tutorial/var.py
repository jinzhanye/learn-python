# coding=utf-8

myStr = 'Hello'
myInt = 25
myFloat = 12.4

myList = [1, 2, 3, '12323']
myList.append(4)
myDict = {'a': 1, 'b': 2, 'c': 3}

print(type(myStr), myStr)
print(type(myInt), myInt)
print(type(myFloat), myFloat)
print(type(myList), myList)
print(type(myDict), myDict)

print(myDict['a'])

# assert expression 等价于
# if not expression:
#     raise AssertionError
# myStr 不是int所以这里会抛出错误
assert type(myStr) == int


# this is wrong: myDict.a

class Person:
    # __ means private
    __name = ''
    __email = ''

    # constructor
    def __init__(self,name, email):
        self.__name = name
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email
