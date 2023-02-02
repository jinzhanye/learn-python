# coding=utf-8
import traceback
import asyncio

# 基础类型
print('\n基础类型*****************************************')
myStr = 'Hello'
myInt = 25
myFloat = 12.4

myList = [1, 2, 3, '12323']
myList.append(4)
myDict = {'a': 1, 'b': 2, 'c': 3}
myTuple = (1, 2, 3, 4, 5 )
mySet = set(("Google", "Runoob", "Taobao"))
mySet.add("Facebook")

print(type(myStr), myStr)
print(type(myInt), myInt)
print(type(myFloat), myFloat)
print(type(myList), myList)
print(type(myTuple), myTuple)
print(type(myDict), myDict)
print(type(mySet), mySet)

print(myDict['a'])
print('myDict.keys()', myDict.keys())
print('myDict.values()', myDict.values())

# assert expression 等价于
# if not expression:
#     raise AssertionError
# myStr 不是int所以这里会抛出错误

# assert type(myStr) == int
# this is wrong: myDict.a

# 面向对象
print('\n面向对象*****************************************')
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

person = Person('luobogo', 'luobogo@gmail.com')

# 会报错：'Person' object has no attribute '__email'
# print('person.__email:', person.__email)

print('person email', person.get_email())

class Mammal(object):
  neo_cortex = True
 
class Cat(Mammal):
  def __init__(self, name, years):
    self.name = name
    self.years = years
 
  def eat(self, food):
    print(f'nom {food}')
 
fry_cat = Cat('Fry', 7)
fry_cat.eat('steak')
print('type fry_cat:', type(fry_cat))

# 判空
print('\n判空*****************************************')
## 对象用 hasattr 判断属性是否存在
catYear = fry_cat.years if hasattr(fry_cat, 'years') else '-'
print('catYear:', catYear)

## 字典用 in  判断
myDictA = myDict['a'] if 'a' in myDict else ''
print('myDictA:', myDictA)

print('\n循环*****************************************')
def print_hi(name, *args):
  # Use a breakpoint in the code line below to debug your script.
  print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
  for index, arg in enumerate(args):
    print(index, arg)

print_hi('hello', 'a', 'b')


# 异常处理
print('\n异常处理*****************************************')

def testException():
  try:
    raise RuntimeError('抛出运行时异常')
  except Exception as ex:
    msg = traceback.format_exc()
    print('异常：', msg)

testException()

# 函数
print('\n函数*****************************************')

def printinfo(name, age):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
## 使用关键字参数允许函数调用时参数的顺序与声明时不一致
printinfo(age=50, name="runoob")


# None，Python中没有NULL，只有None
print('\nNone*****************************************')
def testNone(arg):
  if arg == 1:
    return ''

tesNoneStr1 = testNone(1)
print('tesNoneStr1 == \'\'', tesNoneStr1 == '')
print('tesNoneStr1 == None',tesNoneStr1 == None)

tesNoneStr2 = testNone(2)
print('tesNoneStr2 == \'\'', tesNoneStr2 == '')
print('tesNoneStr2 == None', tesNoneStr2 == None)

# 作用域
print('\n作用域*****************************************')
outter = 10
def testScope1():
  outter = 11
testScope1()
print('testScope1 outter:', outter) ## 10

def testScope2():
  global outter
  outter = 11
testScope2()
print('testScope2 outter:', outter) ## 11