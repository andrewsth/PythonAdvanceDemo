f = abs
print f.__name__
print f(-123)


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print 'My name is %s...' % self.name
        print 'My friend is %s...' % friend


p = Person('Bob', 'male')
p('Tim')


# task

class Fib(object):
    def __call__(self, num):
        self.l = []
        if num == 1:
            self.l.append(0)
            return self.l
        elif num == 2:
            self.l.append(1)
            return self.l
        else:
            a, b = 0, 1
            for i in range(10):
                self.l.append(a)
                a, b = b, a + b
            return self.l


f = Fib()
print f(10)
