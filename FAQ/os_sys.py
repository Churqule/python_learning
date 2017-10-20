#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# os.py

import os
import sys

'''获取当前路径'''
'''当前路径可以用'.'表示,再用os.path.abspath()将其转换为绝对路径'''
print('当前路径为:')
print(os.path.abspath('.'))

'''获取当前模块的文件名'''
print('当前文件名为:')
print(__file__)
print(sys.argv[0])

'''获取命令行参数'''
print('当前命令行参数为:')
print(sys.argv)

'''获取当前Python命令的可执行文件路径'''
print('当前命令可执行文件路径为:')
print(sys.executable)

'''python路径'''
print('当前Python路径为:')
print(sys.path)

'''获取当前对象类型'''
list = []
tuple = ()
dict = {}
set = set([])
print(
    type(list),
    type(tuple),
    type(dict),
    type(set),

)

'''排序'''
a = [1,3,2]
a.sort()
print(a)

'''替换'''
print('aBc'.replace('B','b'))

'''查看函数帮助信息'''
help(abs)

'''取绝对值'''
print(abs(-5))

'''取最大值'''
print(max(1,4,2,-5,0))

'''取最小值'''
print(min(1,4,2,-5,0))

'''其他数据类型转换为整数'''
print(int('123'),int(12.63))

'''其他数据类型转换为字符型'''
print(str(123),str(1.23))

'''其他数据类型转换为浮点数'''
print(float(11))

'''其他数据类型转换为布尔型'''
print(bool(1),bool())

'''其他数据类型转换为16/2/8进制'''
print(hex(255),bin(255),oct(6))

'''数据类型检查可以用内置函数isinstance()实现：'''
print(isinstance('test',(int,float)))
print(isinstance(bool(1),(int,float,list,tuple,dict,set)))
print(type(bool(1)))

'''
使用dir()函数可以查看对像内所有属性及方法，
在python中任何东西都是对像，一种数据类型，一个模块等，都有自己的属性和方法，
除了常用方法外，其它的你不需要全部记住它，交给dir()函数就好了。
'''
print('查看list对象内所有属性及方法:')
print(dir([]))