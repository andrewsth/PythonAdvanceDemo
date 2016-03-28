# class Student(object):
#     __slots__ = ('name', 'gender', 'score')
#
#     def __init__(self, name, gender, score):
#         self.name = name
#         self.gender = gender
#         self.score = score
#
#
# s = Student('Bob', 'male', 59)
# s.name = 'Tim'  # OK
# s.score = 99  # OK
# s.grade = 'A'



# task
class Person(object):
    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):
    __slots__ = ('score')

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score


s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print s.score
