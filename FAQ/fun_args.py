#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os

'''
函数参数:
1.位置参数;
2.默认参数;
3.可变参数;
4.关键字参数;
'''

'''
##########################################1.位置参数;
'''
def power(x,n):
    s=1
    while n >0:
        n = n - 1
        s = s*x
    return s
print(power(3,3))
#函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。

'''
##########################################2.默认参数;
'''
def power(x,n=3):
    s=1
    while n >0:
        n = n - 1
        s = s*x
    return s
print(power(3))
#其中n=3就是默认参数;

'''
默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
二是如何设置默认参数。
当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
定义默认参数要牢记一点：默认参数必须指向不变对象！
'''

'''
##########################################3.可变参数;
在Python函数中，还可以定义可变参数。
顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
'''
'''
我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。

要定义出这个函数，我们必须确定输入的参数。
由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
'''
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
#但是调用的时候，需要先组装出一个list或tuple：
print(calc([1,2,3]))
'''
如果利用可变参数,把函数参数改为可变参数:
'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc(1,2,3))
'''
定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
但是，调用该函数时，可以传入任意个参数，包括0个参数。
'''
#如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums = [1,2,3]
print(calc(nums[0],nums[1],nums[2]))
#Python也允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
print(calc(*nums))
'''
*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
'''

'''
##########################################4.关键字参数

可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Michael',30))
print(person('Bob',35,city='Beijing',job='Engineer'))
#简化方法:
extra = {'city':'Beijing','job':'Engineer'}
print(person('Jack',24,**extra))
'''
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
'''

'''
##########################################5.命名关键字参数
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
'''

def person(name, age, *, city, job):
    print(name, age, city, job)
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
#调用方式如下:
person('Jack', 24, city='Beijing', job='Engineer')

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：

def person(name, age, *args, city, job):
    print(name, age, args, city, job)
print(person('Jack',24,'Man',city='Beijing',job='Engineer'))

'''
使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：

def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass
'''

'''
##########################################6.参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

print(f1(1, 2, 3, 'a', 'b'),
f1(1, 2, 3, 'a', 'b', x=99),
f2(1, 2, d=99, ext=None))

#最神奇的是通过一个tuple和dict，你也可以调用上述函数：
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print(f1(*args, **kw))
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print(f2(*args, **kw))
