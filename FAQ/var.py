#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# var.py

import os

'''###################################字符转义######################################'''

print('I\'m ok.')

''''
比如\n表示换行,\t表示制表符,\\表示字符\
'''
print('I\'m learning\nPython.')
print('\\\n\\')
print('\\\t\\')

'''r''表示''内部的字符串默认不转义'''
print(r'\\\t\\')

'''字符串内部允许用\'\'\'...\'\'\'的格式表示多行内容'''
print('''
line1
line2
line3
''')

'''###################################条件判断######################################'''
age =3
if age >=18:
    print('adult')
else:
    print('teenager')

'''###################################空值######################################'''

'''
空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
此外，Python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型，我们后面会继续讲到。
'''

'''###################################变量######################################'''

'''变量名必须是大小写英文、数字和_的组合,且不能用数字开头'''
a = 'ABC'
print(a)
'''
Python解释器干了两件事情：
在内存中创建了一个'ABC'的字符串；
在内存中创建了一个名为a的变量，并把它指向'ABC'。
'''

'''Python中,通常用全部大写的变量表示常量'''
PI = 3.14159265359
print(PI)

'''
两种除法,一种除法是/,计算结果是浮点数;要做精确的除法,使用/就可以;
还有一种除法是//,称为地板除,结果永远是整数,即使除不尽;
'''
print(10/3)
print(10//3)
print(9/3)

'''余数运算%,可以得到两个整数相除的余数'''
print(10%3)