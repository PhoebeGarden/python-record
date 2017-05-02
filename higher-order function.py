#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#参数可以传函数
def add(x, y, f):
	return f(x)+f(y)

x = -5
y = 6
f = abs
print(add(x, y, f))

#map/reduce

#map函数用于把list中的所有元素按照输入函数进行处理，并返回一个iterator
def f(x):
	return x*x

r = map(f, [1, 2, 3, 4, 5, 6, 7])

#print(list(r))
for x in r:
	print(x)

#reduce, 是把一个函数作用在一个序列上，这个函数必须接受两个参数，
#reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
def fn(x, y):
	return x*10+y
print(reduce(fn, [1, 3, 5, 7, 9]))

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(reduce(fn, map(char2num, '13579')))

#exercise:
def normalize(name):
	return name[0].upper()+name[1:].lower()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
	return reduce(lambda x, y:x*y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def str2float(s):
	dot = s.find('.')
	s = s.replace('.', '')
	return reduce(fn, map(char2num, s))/prod([10]*dot)
    

print('str2float(\'123.456\') =', str2float('123.456'))