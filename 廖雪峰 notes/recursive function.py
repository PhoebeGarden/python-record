#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(1))
print(fact(5))
print(fact(100))
#为了防止递归栈溢出，需要通过尾递归优化
#尾递归是指，在函数返回的时候只调用自身本身，上面的函数不是，因为返回的是乘积
def fact(n):
	return fact_iter(n,1)
def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num-1, num*product)
#fact(1000) 大部分语言都没有针对为递归优化，因此还是不行。。。。所以这一点真是醉了

#exercise 汉诺塔
def move(n, a, b, c):
	if n == 1:
		print(a,'-->', c)
		return
	else:
		move(n-1, a, c, b)
		print(a, '-->', c)
		move(n-1, b, a, c)

move(3, 'A', 'B', 'C')