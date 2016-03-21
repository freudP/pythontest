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
#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
print(calc(*nums))
print('\n')

#关键字参数,关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    return('name:', name, 'age:', age, 'other:', kw)

print(person('Adam', 45, gender='M', job='Engineer'))


def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    return('name:', name, 'age:', age, 'other:', kw)

print( person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))

#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, **extra))

#限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数,和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
#使用命名关键字参数时，要特别注意，*不是参数，而是特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
def person(name, age, *, city, job):
    return (name, age, city, job)
print(person('Jack', 24, city='Beijing', job='Engineer'))
#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
#print(person('Jack', 24, 'Beijing', 'Engineer'))

#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用，除了可变参数无法和命名关键字参数混合。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    return ('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    return ('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
print('可变参数无法和命名关键字参数混合')
print(f1(1,2))
print(f1(1,2,c=3))#默认参数传值
print(f1(1,2,3,'a','b'))#可变参数传值list or tuple
print(f1(1,2,3,'a','b', x= 99))#关键数参数传值dict
print(f2(1,2,d=99,ext=None))#命名关键字参数传值
print('\n')
print('#用list和tuple，调用函数')
args = (1, 2, 3, 4)
kw = {'d':99,'x':'#'}
print(f1(*args,**kw))
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print(f2(*args, **kw))

print('''
小结:
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
要注意定义可变参数和关键字参数的语法：
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数不要忘了写分隔符*，否则定义的将是位置参数。
''')
