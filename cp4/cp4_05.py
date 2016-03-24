# class Person(object):
#     def __init__(self, name):
#         self.name = name
#         self._title = 'Mr'
#         self.__job = 'Student'
#
#
# p = Person('Bob')
# print p.name
#
# print p._title

# print p.__job


# task
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score


p = Person('Bob', 59)

print p.name
try:
    print p.__score
except AttributeError, e:
    print 'attributeerror'
