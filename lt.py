# -*- coding: utf-8 -*-
#创建list
'''
l = ['a', 'b', 'c']
#print list
print(l)
#print list length
print(len(l))
print(l[0],l[1],l[2],l[-1],l[-2],l[-3])
#插入元素
l.insert(0,'A')
print(l)
#删除元素
l.pop(0)
print(l)
#替换元素
l[0] = 'A'
print(l)

#不同类型元素的list
l = ['str', 123, True]
print(l)
#list中套list
l = ['c',['java', 'c#'], ['php', 'python', 'perl']]
print(l)
print(len(l))
p = l[2]
print(p[1])

p = ['python','php','perl']
s = ['java','c#']
l = ['c', p , s]
print(l)
print(l[0],p[0])
'''

#创建tuple
t = ('a',123,True,)
print(t)
print(t[-1])

t = ('a', ['a','b'])
t[1][0] = 'x'
t[1][1] = 'y'
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])