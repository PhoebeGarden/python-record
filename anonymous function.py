#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#匿名函数，之前也用过：lambda

def fn1():
	x, y = 1, 2
	return lambda : x + y
print(fn1()())

def fn2():
	x, y = 1, 2
	return lambda x, y : x + y
print(fn2()(3, 4))

def fn3():
	x, y = 1, 2
	return lambda x = x, y = y: x + y
print(fn3()())