#/usr/bin/evn python
# -*- coding: utf-8 -*-

from abstest import my_abs
print(my_abs(34))

'''
n = float(input('n='))
print(isinstance(n,int))
print(isinstance(n,float))
#print(type(eval(n)))

>>> a = 123
>>> b = 123.321
>>> isinstance(a, int)
True
>>> isinstance(b, float)
True
>>> isinstance(a, float)
False
>>>
type(eval("123")) == int
type(eval("123.23")) == float

'''

import  math

def move(x,y,step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x,y)
r = move(100, 100, 60, math.pi / 6)
print(r)

#Practice
#注意：定义函数时，返回值一定要用return，否则会返回None。
def quadratic(a,b,c):
    #实例抽象
    delta = b*b - 4*a*c
    #数学逻辑：a≠0,才有意义，△=0,《0，》0三种情况下一元二次方程的根分别是多少。
    if a != 0:
        if delta < 0:
            return('no real root')
        elif delta == 0:
            x = -b / (2 * a)
            return('only one repeated root: %.1f ' % x)
        else:
            x1 =(-b + math.sqrt(delta)) / (2 * a)
            x2 =(-b - math.sqrt(delta)) / (2 * a)
            #注：字符串格式化格式，一个%占位符可以省略（），2个以上必须加（）。
            return('tow real roots: (%.1f,%.1f)'% (x1, x2))
    else:
        return('a vlues is not equal to zero!')


print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)
#print(quadratic(0,2,3)) # => a vlues is not equal to zero!

#默认参数
#默认参数必须指向不变对象
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2,3))
print(power(5))

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

print(enroll('Sarah', 'F'),'\n')
print(enroll('Bob', 'M', 7),'\n')
print(enroll('Adam', 'M', city='Tianjin'))

#默认参数必须指向不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())
print('\n')

#可变参数,参数前面加*号，参数接收到一个tuple,可以传入任意个参数，包括0个参数。
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1,2,3]))
print(calc((1,3,5,7)))

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3))
print(calc(1,3,5,7))
print(calc())
#已经有一个list或者tuple，要调用一个可变参数.Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1, 2, 3]
print(calc(nums[0],nums[1],nums[2]))
print(calc(*nums))
print('\n')

#关键字参数,关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

