#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#generator的引入，不必创建完整的list时，节省空间
L = [x*x for x in range(10)]
print("L =", L)
g = (x*x for x in range(10))
print("g =", g);
#generator的打印
for n in g:
	print(n)

#斐波拉契数列
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a+b
		n = n + 1
	return 'done'

fib(6)

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b
		n = n + 1
	return 'done'

g = fib(6)
print(g)
#for n in g:
#	print("generator:", n)

#for循环的方式拿不到generator的返回值，用下面的方法拿到返回值
while True:
	try:
		x = next(g)
		print("x :", x)
	except StopIteration as e:
		print("Generator return value:", e.value)
		break

#exercise
def triangles():
	L = [1]
	while True:
		yield L
		l = [1]
		l = l + [L[n]+L[n+1] for n in range(len(L)-1)] + [1]
		L = l
		

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break