#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# fun.py

import os

'''
在Python中，定义一个函数要使用def语句，
依次写出函数名、括号、括号中的参数和冒号:，
然后，在缩进块中编写函数体，函数的返回值用return语句返回。
'''
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

'''
请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
return None可以简写为return。
在Python交互环境中定义函数时，注意Python会出现...的提示。函数定义结束后需要按两次回车重新回到>>>提示符下：
'''

'''
如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，
用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）：
'''

'''
空函数

如果想定义一个什么事也不做的空函数，可以用pass语句：
'''
def nop():
    pass

'''
pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
'''