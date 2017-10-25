#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os

'''###################################list######################################'''

classmates = ['Michael', 'Bob', 'Tracy']
print(type(classmates))
print(classmates)
print(len(classmates))
print(classmates[0])

'''如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：'''
print(classmates[-1])

'''索引值获取:'''
print(classmates.index('Bob'))

'''往list中追加元素到末尾：'''
classmates.append('Adam')
print(classmates)

'''把元素插入到指定的位置，比如索引号为1的位置：'''
classmates.insert(1,'Jack')
print(classmates)

'''要删除list末尾的元素，用pop()方法：'''
classmates.pop()
print(classmates)

'''删除指定位置的元素，用pop(i)方法，其中i是索引位置：'''
classmates.pop(1)
print(classmates)

'''把某个元素替换成别的元素，可以直接赋值给对应的索引位置：'''
classmates[1] = 'Sarah'
print(classmates)

'''list元素也可以是另一个list，比如：'''
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))

'''如果一个list中一个元素也没有，就是一个空的list，它的长度为0：'''
L = []
print(len(L))

'''###################################tuple######################################'''
'''另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：'''
classmates = ('Michael','Bob','Tracy')
print(type(classmates))

'''
不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来。
'''

'''如果要定义一个空的tuple，可以写成()：'''
t = ()
print(t)

'''
定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义。
因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
'''
t = (1)
print(t)
t = (1,)
print(t)

'''最后来看一个“可变的”tuple：'''
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

'''
表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
'''