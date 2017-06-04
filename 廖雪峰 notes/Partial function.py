#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#functools.partial 帮助我们创建一个偏函数
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))