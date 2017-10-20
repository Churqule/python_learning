#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os

'''
练习1
请打印出以下变量的值：
'''

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

'''
练习

小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
'''
s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('%2.1f%%' % r)

'''
练习

请用索引取出下面list的指定元素：
'''
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

'''
练习

小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：
'''
height = 1.75
weight = 80.5
bmi = weight/(height*height)
print(bmi)
if bmi < 18.5:
    print('体重过轻')
elif bmi >= 18.5 and bmi < 25:
    print('体重正常')
elif bmi >= 25 and bmi < 28:
    print('体重过重')
elif bmi >=28 and bmi <32:
    print('体重肥胖')
else:
    print('体重严重肥胖')

'''
练习

请利用循环依次对list中的每个名字打印出Hello, xxx!：
'''
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,%s!' % name)

'''
练习

请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
ax2 + bx + c = 0
的两个解。
提示：计算平方根可以调用math.sqrt()函数：
'''