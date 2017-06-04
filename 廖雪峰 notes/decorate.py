#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def now():
	print("2017-6-4")
f = now
f()
print(now.__name__)
print(f.__name__)

#在函数调用前后自动打印日志，但又不希望修改now（）函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”

#把@log放到now（）函数的定义处，相当于执行了语句now=log(now)
def log(func):
	def wrapper(*args, **kw):
		print('call %s():' %func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print("2017-06-04")
now()

#三层嵌套的decorator用法：
def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' %(text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print('2015-3-25')

now()

#完整的写法
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

import functools
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s()' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

#练习1
def printBECall(func):
	def wrapper(*args, **kw):
		print('begin call %s():' % func.__name__)
		func(*args, **kw)
		print('end call %s():' % func.__name__)
	return wrapper

@printBECall
def now():
	print('2015-3-25')

now()

#练习二
def log(text=None):
	def decorator(func):
		def wrapper(*args, **kw):
			if None == text:
				print('log %s():' %(func.__name__))
			else:
			    print('%s %s():' %(text, func.__name__))
			
			return func(*args, **kw)
		return wrapper
	return decorator

@log('text')
def now():
	print('2015-3-25')

now()