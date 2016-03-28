from __future__ import division


class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return self.p / self.q


print int(12.34)

print float(12)

r = Rational(12, 5)
n = int(r)

print int(Rational(7, 2))

print int(Rational(1, 3))

print float(Rational(7, 2))
print float(Rational(1, 3))
