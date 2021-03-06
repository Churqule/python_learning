#!/usr/bin/env python3
#表示.py文件的运行环境;

# _*_ coding:utf-8 _*_
#表示.py文件本身使用标准UTF-8编码；

' a test module '
#表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

__author__ = 'Tzicheng Chew'

import os
import sys

#sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称

'''
为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，
这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。
在Python中，一个.py文件就称之为一个模块（Module）。
'''

'''
使用模块有什么好处？

最大的好处是大大提高了代码的可维护性。其次，编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。
我们在编写程序的时候，也经常引用其他模块，包括Python内置的模块和来自第三方的模块。

使用模块还可以避免函数名和变量名冲突。
相同名字的函数和变量完全可以分别存在不同的模块中，因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。
但是也要注意，尽量不要与内置函数名字冲突。点这里查看Python的所有内置函数。

你也许还想到，如果不同的人编写的模块名相同怎么办？
为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。
'''

'''
假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。
方法是选择一个顶层包名，比如mycompany，引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。
现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。
请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。
'''

'''
自己创建模块时要注意命名，不能和Python自带的模块名称冲突。
例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。
'''
def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
#最后，注意到这两行代码：
if __name__=='__main__':
    test()

'''
当我们在命令行运行module模块文件时，Python解释器把一个特殊变量__name__置为__main__，
而如果在其他地方导入该hello模块时，if判断将失败，
因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
'''

'''
##############################################作用域
在Python中，有的函数和变量我们希望仅仅在模块内部使用,是通过_前缀来实现的。
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，
是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。

private函数或变量不应该被别人引用，那它们有什么用呢？
外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
'''