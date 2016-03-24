# class Person(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def get_grade(self):
#         return 'A'
#
#
# p1 = Person('Bob', 90)
# print p1.get_grade
#
# print p1.get_grade()

import types


# def fn_get_grade(self):
#     if self.score >= 80:
#         return 'A'
#     if self.score >= 60:
#         return 'B'
#     return 'C'
#
#
# class Person(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#
# p1 = Person('Bob', 90)
# p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
# print p1.get_grade()
#
# p2 = Person('Alice', 65)
# print p2.get_grade()


class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'


p1 = Person('Bob', 90)
print p1.get_grade
print p1.get_grade()
