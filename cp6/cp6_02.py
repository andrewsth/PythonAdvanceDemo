class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)

    __repr__ = __str__


p = Person('Bob', 'male')
print p


# task
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(Student:%s,%s,%s)' % (self.name, self.gender, self.score)

    __repr__ = __str__


s = Student('Bob', 'male', 88)
print s
