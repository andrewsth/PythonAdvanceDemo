# class Person(object):
#     address = 'Earth'
#
#     def __init__(self, name):
#         self.name = name
#
#
# print Person.address
#
# p1 = Person('Bob')
# p2 = Person('Alice')
# print p1.address
#
# print p2.address
#
# Person.address = 'China'
# print p1.address
#
# print p2.address


# task

class Person(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1


p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count

p3 = Person('Tim')
print Person.count
