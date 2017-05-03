#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#函数作为返回值，例如求和函数，不需要立即求和，
#而是在后面的运行过程中，根据需要再计算

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f())
#这种结构也称为闭包
#闭包需要特别注意变量有效的范围，返回函数不要饮用任何循环变量，或者后续会发生变化的变量！！
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1, f2, f3 = count()
print('f1() = ', f1())
print('f2() = ', f2())
print('f3() = ', f3())

def count():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs
f1, f2, f3 = count()
print('f1() = ', f1())
print('f2() = ', f2())
print('f3() = ', f3())
