# _*_ coding:utf-8 _*_


def f(x):
    return x * x


print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print map(f, range(1, 10))


# task
def format_name(s):
    return s[0].upper() + s[1:].lower()


print map(format_name, ['adam', 'LISA', 'barT'])
