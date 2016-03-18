# _*_ coding:utf-8_*_
import math


def add(x, y, f):
    return f(x) + f(y)


print add(-5, 9, abs)

# task
print add(25, 9, math.sqrt)
