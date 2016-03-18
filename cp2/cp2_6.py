# _*_ coding:utf-8_*_
import math


def is_odd(x):
    return x % 2 == 1


print filter(is_odd, [1, 4, 6, 7, 9, 12, 17])


def is_not_empty(s):
    return s and len(s.strip()) > 0


print filter(is_not_empty, ['test', None, '', 'str', '   ', 'END'])

a = '\t\n123\r\n'
print a.strip()


# task

def is_sqr(x):
    return math.sqrt(x) % 1 == 0


print filter(is_sqr, range(1, 101))
