# _*_ coding:utf-8_*_

print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print sorted([1, 3, 9, 5, 0], lambda x, y: -cmp(x, y))

myabs = lambda x: -x if x < 0 else x
print myabs(-1)


# task
def is_not_empty(s):
    return s and len(s.strip()) > 0


print filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])
