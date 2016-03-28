# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score
#
#     def get_score(self):
#         return self.__score
#
#     def set_score(self, score):
#         if score < 0 or score > 100:
#             raise ValueError('invalid score')
#         self.__score = score
#
#
# s = Student('Bob', 59)
#
# s.set_score(60)
# s.set_score(1000)


# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score
#
#     @property
#     def score(self):
#         return self.__score
#
#     @score.setter
#     def score(self, score):
#         if score < 0 or score > 100:
#             raise ValueError('invalid score')
#         self.__score = score
#
#
# s = Student('Bob', 59)
# s.score = 60
# print s.score
# s.score = 1000


# task
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        if self.score >= 80:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


s = Student('Bob', 59)
print s.grade

s.score = 60
print s.grade

s.score = 99
print s.grade
