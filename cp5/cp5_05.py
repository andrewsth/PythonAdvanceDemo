class A(object):
    def __init__(self, a):
        print 'init A...'
        self.a = a


class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init B...'


class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init C...'


class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init D...'


class Person(object):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class SkillMixin(object):
    pass


class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'


class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'


class BStudent(BasketballMixin, Student):
    pass


class FTeacher(FootballMixin, Teacher):
    pass


s = BStudent()
print s.skill()

t = FTeacher()
print t.skill()
