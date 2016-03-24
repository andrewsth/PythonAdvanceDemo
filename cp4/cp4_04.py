# class Person(object):
#     def __init__(self, name, gender, birth):
#         self.name = name
#         self.gender = gender
#         self.birth = birth
#
#
# xiaoming = Person('Xiao Ming', 'Male', '1991-1-1')
# xiaohong = Person('Xiao Hong', 'Female', '1992-2-2')
#
# print xiaoming.name
#
# print xiaohong.birth

# task


class Person(object):
    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for k, v in kw.iteritems():
            setattr(self, k, v)


xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job
