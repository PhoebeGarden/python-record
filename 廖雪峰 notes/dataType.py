#!/usr/bin/env python3
# -*- coding: utf-8 -*-


a = 100
if a >= 0:
	print(a);
else:
	print(-a)

print('i\'m ok.')
print('\'')
print(r'\'')
print('''line1
line2
line3''')

print('True is',True)
print('False is',False)
print('True or False is' , True or False)
print('True and False is' , True and False)
print('not True is', not True)
print(None) #无意义，不等同于0

print(9/3)
print(9//3)
print(10%3)

s4=r'''Hello,
Lisa!'''
print(s4)

print('包含中文的str')
print('A 的整数表示是', ord('A'))
print('中的整数表示是', ord('中'))
print('B的字符表示是', chr(66))
print('25991的字符表示是', chr(25991))
print('\'\\u4e2d\\u6587\'的字符表示','\u4e2d\u6587')

x=b'ABC'
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
#print('中文'.encode('ascii'))

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len(b'ABC'))
print(len('中文'))
print(len('中文'.encode('utf-8')))

print('Hi, %s, you have $%d.' %('Phoebe', 100000))
print('%-2d-%02d' % (3,1))
print('%.2f' % 3.1415926)
print('growth rate: %d %%' % 7)

#练习
s1 = 72
s2 = 85
r = (85-72)/72*100
print('小明成绩提高 %.1f' % r)