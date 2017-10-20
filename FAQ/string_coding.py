#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os

'''###################################字符串编码######################################'''

'''
在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言;
'''
print('包含中文的str')

'''
对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
'''
print(ord('A'))
print(ord('中'))

print(chr(66))
print(chr(25991))


'''Python对bytes类型的数据用带b前缀的单引号或双引号表示：'''
x = b'ABC'
y = 'ABC'
print(type(x))
print(type(y))

'''以Unicode表示的str通过encode()方法可以编码为指定的bytes'''
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

'''反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：'''
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

'''len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：'''
print(len(b'ABC'))
print(len('ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

'''
可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
'''

'''###################################格式化######################################'''
'''在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：'''
print('Hello,%s' % 'world')
print('Hi,%s,you have $%d.' % ('Michael',100000))

'''
%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。
如果只有一个%?，括号可以省略。
常见的占位符有：
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
'''
'''格式化整数和浮点数还可以指定是否补0和整数与小数的位数：'''
print('%2d-%02d' % (3,1))
print('%.2f' % 3.1415926)

'''有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：'''
print('growth rate: %d%%' % 7)
