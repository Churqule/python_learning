#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os

'''
Python内建了map()和reduce()函数。

如果你读过Google的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，
你就能大概明白map/reduce的概念。

########################################map函数
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
'''
def f(x):
    return x*x
r = map(f,[1,2,3,4])
print(list(r))

'''map()传入的第一个参数是f，即函数对象本身。
由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
所以，map()作为高阶函数，事实上它把运算规则抽象了，
因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
'''
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

'''
########################################reduce函数
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

比方说,把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
'''
from functools import reduce
def fn(x,y):
    return x*10 + y
print(reduce(fn,[1,3,5,7,9]))

'''
########################################map+reduce函数结合使用
这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，
对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
'''
from functools import reduce
def fn(x,y):
    return x*10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(reduce(fn,list(map(char2num,'13579'))))