#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#函数调用 练习
n1 = 255
n2 = 1000
print(str(hex(n1)))
print(str(hex(n2)))

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

my_abs(1)

#函数返回多个值的时候其实是返回一个tuple！！
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

def quadratic(a, b, c):
	return (-b+math.sqrt(b*b-4*a*c))/2/a, (-b-math.sqrt(b*b-4*a*c))/2/a 

x1, x2 = quadratic(2, 3, 1)
print('x1 =', x1, ', x2 =', x2)

x1, x2 = quadratic(1, 3, -4)
print('x1 =', x1, ', x2 =', x2)

#函数默认值, 默认值也是变量， 会根据每次调用修改
def add_end(L=[]):
    L.append('END')
    return L
L = add_end()
print(L);
L = add_end()
print(L);
#定义成如下即可
print('修改默认参数的处理，把默认参数改回原来的值')
def add_end(L= None):
    if L is None:
    	L = []
    L.append('END')
    return L
L = add_end()
print(L);
L = add_end()
print(L);

#可变参数
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc(1, 2))

#list tuple 可以用加上*的方式直接变成变参传入变参函数中
nums = [1, 2, 3]
print(calc(*nums))


#关键字参数
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city':'Beijing', 'job':'Engineer'}
person('Jack', 24, **extra)

#命名关键字参数
def person(name, age, **kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:', name, 'age:', age, 'other:', kw)
person('Jack', 24, city='Beijing', addr='Chaoyang', 
	zipcode=123456)

#限制关键字参数的名字
def person(name, age, *, city, job):
	print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')

#如果函数中已经定义了一个可变参数，
#后面跟着的命名关键字参数就不用特殊分隔符*
def person(name, age, *args, city, job):
	print(name, age, args, city, job)
person('Jack', 24, city='Beijing', job='Engineer')
#person('Jack', 24, 'Beijing', 'Engineer')  这种调用方式会报错

#参数组合的顺序一定是:必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1, 2)
f1(1, 2, c=3)	
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d' : 99, 'x' : '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d' : 88, 'x' : '#'}
f2(*args, **kw)