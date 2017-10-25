#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os

'''
汉诺塔的移动可以用递归函数非常简单地实现。

请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
然后打印出把所有盘子从A借助B移动到C的方法，例如：
'''

'''
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：

>>> L = ['Hello', 'World', 18, 'Apple', None]
>>> [s.lower() for s in L]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <listcomp>
AttributeError: 'int' object has no attribute 'lower'
使用内建的isinstance函数可以判断一个变量是不是字符串：
请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
'''
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s,str)])

'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
'''
def normalize(name):
    return name[0].upper()+name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

'''
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''
from functools import reduce
def prod(L):
    def mup(x,y):
        return x*y
    return reduce(mup,L)

print('3*5*7*9 =',prod([3,5,7,9]))

'''
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
'''
from functools import reduce
def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    def num2int(x,y):
        return x*10+y
    i = s.index('.')

    return reduce(num2int,list(map(char2num,s[:i]))) + reduce(num2int,list(map(char2num,s[i+1:])))/pow(10,len(s[i+1:]))

print(str2float('123.456'))

