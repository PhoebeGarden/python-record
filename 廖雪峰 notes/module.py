#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#这个测试时需要在python环境测试的，可以带变量运行python，结果将会因带的变量格式而导致结果不同
'a test module'

__author__ = 'Phoebe Liu'

import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' %args[1])
    else:
        print('Too many arguments!')

if __name__== '__main__':
	test()

#作用域
#私有变量或函数用_表示，一般不要直接访问（但是不是不能直接访问）

#安装第三方模块
from PIL import Image
im = Image.open('294561.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('thumb.jpg','JPEG')

#运行时修改环境变量
import sys
sys.path.append('/Users/michael/my_py_scripts')