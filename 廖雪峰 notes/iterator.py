#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#可用于for循环的对象统称为可迭代对象，
#可用户next()函数不断调用并返回下一个值的对象成为迭代器：Iterator
from collections import Iterable

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

#虽然list dict str都不是iterator对象，但可以被迭代
from collections import Iterator
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(100, Iterator))

#可以通过iter()函数将可被迭代的数据转换为迭代器

print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

#python的for循环就是根据iter()后的迭代器实现的