class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name


print type(123)

s = Student('Bob', 'Male', 88)
print type(s)

print dir(123)
print dir(s)

print getattr(s, 'name')
setattr(s, 'name', 'Adam')
print s.name

try:
    getattr(s, 'age')
except:
    print 'cannot getattr for age'

print getattr(s, 'age', 20)


# task
class Person(object):
    def __init__(self, name, gender, **kw):
        for k, v in kw.iteritems():
            self.__setattr__(k, v)


p = Person('Bob', 'Male', age=18, course='Python')
print p.age
print p.course
