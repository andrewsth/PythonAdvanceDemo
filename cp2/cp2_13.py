# _*_coding:utf-8_*_
import time


def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)

        return wrapper

    return log_decorator


@log('DEBUG')
def test():
    pass


print test()


# task
def performance(unit):
    def performance_inside(f):
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


print factorial(10)
