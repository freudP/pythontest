# -*- coding: utf-8 -*-
'''
age = int(input("Please your age: "))

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

'''

height = float(input("请输入身高(米):"))
weight = float(input("请输入体重(kg):"))
bmi = int(weight / (height * height))
print('BMI指数为：%d'%bmi)

if bmi < 18.5:
    print('过轻')
elif bmi > 18.5 and bmi < 25:
    print('正常')
elif bmi > 25 and bmi < 28:
    print('过重')
elif bmi > 28 and bmi < 32:
    print("肥胖")
else:
    print('严重肥胖')
