#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#list
classmates = ['Pheobe', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
for x in range(len(classmates)) :
	print('classmates[%d] = ' % x, classmates[x])
	print('classmates[%d] = ' % -x, classmates[-x])

classmates.append('Cherry')
print(classmates)
classmates.insert(1, 'Jack')
print(classmates)
classmates.pop(2) #classmates.pop()就是指的只删除最后一个
print(classmates)
classmates[2] = 'Sarah'
print(classmates)

#list里面元素类型也可以是不同的

#tuple tuple一旦定义了之后不可变
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
t =()
print(t)
t = (1)
print(t)
t = (1,)
print(t)
#可变'tuple',需要借助list
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

#练习
L = [
    ['Apple', 'Google', 'Microsofg'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])