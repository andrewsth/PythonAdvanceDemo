# _*_ coding:utf-8_*_


def f():
    print 'call f()...'

    # 定义函数g
    def g():
        print 'call g()...'

    # 返回函数g
    return g


x = f()
print x
x()


def myabs():
    return abs


f1 = myabs()
print f1(-1)


def myabs2(x):
    return abs(x)


print myabs2(-9)


def calc_sum(lst):
    return sum(lst)


print calc_sum([1, 2, 3, 4])


def calc_sum(lst):
    def lazy_sum():
        return sum(lst)

    return lazy_sum


f = calc_sum([1, 2, 3, 4])
print f
print f()


def calc_prod(lst):
    def lazy_prod():
        def prod(x, y):
            return x * y

        return reduce(prod, lst)

    return lazy_prod


f = calc_prod([1, 2, 3, 4])
print f()
