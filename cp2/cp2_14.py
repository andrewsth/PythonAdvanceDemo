# _*_ coding:utf-8 _*_
import time, functools


def performance(unit):
    def performance_inside(f):
        @functools.wraps(f)
        def func_inside(*args, **kw):
            starttime = time.time()
            result = f(*args, **kw)
            endtime = time.time()
            print 'call %s() in %f %s' % (f.__name__, (endtime - starttime), unit)
            return result

        return func_inside

    return performance_inside


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial.__name__
