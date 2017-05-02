#!/usr/bin/env python3
# -*- coding:utf-8 -*-
d = {'Michael' : 95, 'Bob' : 75, 'Tracy': 85}
print(d['Michael'])

#判断元素是否在dict里
print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas', -1))
print(d.pop('Bob'))
print(d)

#set

s = set([1, 1, 2, 2, 3, 3])
print(s)
s.add(4)
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

#变量和不可变量
a = ['c', 'b', 'a']
a.sort()
print(a)
a = 'abca'
b = a.replace('a', 'A')
print(a)
print(b)

#tuple居然可以作为dict的key！！！
d = {(1, 2, 3):'a'}
print(d)
print(d[(1, 2, 3)])
#set里面也可以用tuple这种不可变量
s = set((1, 1))
print(s)