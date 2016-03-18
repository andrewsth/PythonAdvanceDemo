# _*_ coding:utf-8_*_
import time


def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)

    return fn


@log
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial(10)


def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)

    return fn


@log
def add(x, y):
    return x + y


print add(1, 2)


# task
def performance(f):
    def fn(x):
        starttime = time.time()
        result = f(x)
        endtime = time.time()
        print 'call %s() in %f ms' % (f.__name__, (endtime - starttime))
        return result

    return fn


@performance
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial(10)
