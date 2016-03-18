# _*_ coding:utf-8_*_


def f():
    print 'f()...'

    def g():
        print 'g()...'

    return g


def calc_sum(lst):
    def lazy_sum():
        return sum(lst)

    return lazy_sum


# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    print fs
    return fs


f1, f2, f3 = count()

print f1(), f2(), f3()


# task
def count():
    fs = []

    for i in range(1, 4):
        def f(j=i):
            return j * j

        fs.append(f)

    return fs


f1, f2, f3 = count()

print f1(), f2(), f3()
