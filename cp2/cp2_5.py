# _*_ coding:utf-8 _*_


def f(x, y):
    return x + y


print reduce(f, [1, 3, 5, 7, 9])
print reduce(f, [1, 3, 5, 7, 9], 100)


# task
def prod(x, y):
    return x * y


print reduce(prod, [2, 4, 5, 7, 12])
