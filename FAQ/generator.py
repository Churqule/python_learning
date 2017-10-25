#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os

'''
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
'''
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
print(type(g))

'''
创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？
如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
'''
print(next(g))
'''generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，
直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
'''
from collections import Iterable
print(isinstance(g,Iterable))
#使用for循环，因为generator也是可迭代对象:
for n in g:
    print(n)
'''
所以，我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。
generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
'''
#斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
'''
注意，赋值语句：
a, b = b, a + b
相当于：
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
但不必显式写出临时变量t就可以赋值。
'''
#上面的函数可以输出斐波那契数列的前N个数：
print(fib(6))

'''
上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：

这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(6)
print(type(fib),type(f))

'''
这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

举个简单的例子，定义一个generator，依次返回数字1，3，5：
'''
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

#调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
o = odd()
print(next(o),next(o),next(o))

'''
可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。
执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。

回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
'''