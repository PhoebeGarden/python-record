#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Student(object):
	"""docstring for ClassName"""
	def __init__(self, name, score):
		self.__name=name
		self.__score=score
	def print_score(self):
	    print('%s: %s' % (self.__name, self.__score))
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	def set_score(self, score):
		self.__score=score

bart = Student('Bart Simpson', 98)
bart.print_score()
bart.set_score(94)
bart.print_score()
print(bart._Student__name)
bart.__name="hi"
bart.print_score()
print(bart._Student__name)
print(bart.__name)

#__name会被某一些解释器改成_Student__name，但这种做法不建议，其他python解释器可能不是这种做法

import types
print(type(123))
print(type('123'))
print(type(None))
print(type(bart))
def fn():
	pass
print(type(fn))
print(type(abs))
print(type(lambda x:x))
print(type((x for x in range(10))))

print(isinstance('123', str))
print(isinstance(b'a', bytes))
print(isinstance((1, 2, 3), (list, tuple)))

print(dir('ABC'))

print(len('ABC'))
print('ABC'.__len__())

class MyObject(object):
	def __init__(self):
		self.x=9
	def power(self):
		return self.x*self.x
obj = MyObject()

print(hasattr(obj,'x'))
print(hasattr(obj,'y'))
setattr(obj, 'y', 19)
print(hasattr(obj,'y'))
print(getattr(obj,'y'))
print(getattr(obj,'z', 404))

class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name
	name = 'Student'
s = Student('Bob')
s.score = 90
print(s.name)
del s.name
print(s.name)
