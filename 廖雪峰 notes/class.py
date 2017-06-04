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