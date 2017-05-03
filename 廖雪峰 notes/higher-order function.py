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


#filter函数，用于过滤序列，它把传入的函数一次作用于每个元素，
#然后根据返回值是true还是false决定保留还是丢弃该元素

#把一个序列中的偶数删掉，只留下奇数
def is_odd(n):
	return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

#把一个序列中的空字符串删掉
def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty, [' A', '', 'B', None, 'C', ' '])))

#用filter求素数， 埃氏筛法
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x:x%n > 0

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n  = next(it)
		yield n
		it = filter(_not_divisible, it)

for n in primes():
	if n < 1000:
		print(n)
	else:
		break

#exersize 回数
def is_palindrome(n):
	return str(n) == str(n)[::-1]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))

#sorted函数
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
#反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

#exercise
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]
L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
	return t[1]
L2 = sorted(L, key=by_score, reverse=True)
print(L2)