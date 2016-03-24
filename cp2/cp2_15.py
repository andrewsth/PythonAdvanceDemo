# _*_coding:utf-8_*_
import functools

print int('12345')

print int('12345', base=8)

print int('12345', 16)

# def int2(x, base=2):
#     return int(x, base)
#
# print int2('1000000')
#
# print int2('1010101')

int2 = functools.partial(int, base=2)
print int2('1000000')

print int2('1010101')


def cmp_ignore_case(s1, s2):
    return cmp(s1.lower(), s2.lower())


sorted_ignore_case = functools.partial(sorted, cmp=cmp_ignore_case)
# sorted_ignore_case = functools.partial(sorted, cmp=lambda first, second: cmp(first.lower(), second.lower()))

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])
