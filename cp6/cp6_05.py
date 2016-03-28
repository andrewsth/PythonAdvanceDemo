# class Rational(object):
#     def __init__(self, p, q):
#         self.p = p
#         self.q = q
#
#
# class Rational(object):
#     def __init__(self, p, q):
#         self.p = p
#         self.q = q
#
#     def __add__(self, r):
#         return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
#
#     def __str__(self):
#         return '%s/%s' % (self.p, self.q)
#
#     __repr__ = __str__
#
#
# r1 = Rational(1, 3)
# r2 = Rational(1, 2)
# print r1 + r2


# task


def gcd(m, n):
    if m < n:
        m, n = n, m
    if m % n != 0:
        return gcd(n, m % n)
    else:
        return n


class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        r = gcd(self.p, self.q)
        return '%s/%s' % (self.p / r, self.q / r)

    __repr__ = __str__


r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2
