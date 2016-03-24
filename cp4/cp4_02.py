class Person(object):
    pass


xiaoming = Person()
xiaohong = Person()

print xiaoming
print xiaohong

print xiaoming == xiaohong
print xiaoming is xiaohong
print isinstance(xiaoming, Person)
