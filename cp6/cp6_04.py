class Fib(object):
    def __init__(self, num):
        self.result = []
        a, b = 0, 1
        for index in range(num):
            self.result.append(a)
            a, b = b, a + b

    def __str__(self):
        return self.result.__str__()

    def __len__(self):
        return len(self.result)


f = Fib(10)
print f
print len(f)
