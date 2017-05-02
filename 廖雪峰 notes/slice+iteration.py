#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[:3])
print(L[-3:])
print(L[::2])#每两个取一个

#slice功能可以使用在list、tuple、string，取元素后，仍然保持原来的变量类型

#Iteration
#只要是可迭代对象都可以用for循环
#判断是否是一个可迭代对象
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

L = ['A', 'B', 'C']
for i, value in enumerate(L): #enumerate函数用来把一个list编程索引-元素对
	print(i, value)

#列表生成式
print([x*x for x in range(1,10) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

#列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')])

#dict的items()可以同时迭代key和value
d = {'x':'A', 'y':'B', 'z':'C'}
for k, v in d.items():
	print(k, '=', v)

print([k + '=' + v for k, v in d.items()])
#把list中的所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

#exercise 
#如果一个list中既包含字符串，又包含整数，如何把这个list中的字符串全部改成小写
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])
