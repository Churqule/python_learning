#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os

'''
列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
'''
print(list(range(1,11)))

'''生成[1x1, 2x2, 3x3, ..., 10x10]列表的两种方法:'''
#方法1:
L = []
for x in range(1,11):
    L.append(x*x)
print(L)

#方法2:(列表生成式)
print([x*x for x in range(1,11)])

'''
写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
'''
print([x*x for x in range(1,11) if x%2 == 0])

#还可以使用两层循环,可以生成全排列:
print([m+n for m in 'ABC' for n in 'XYZ'])

#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
print([d for d in os.listdir('.')])

#列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])