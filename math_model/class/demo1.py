# class 也就是结构体
class Person(object):
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return self.first + ' ' + self.last


person = Person('huai', 'xu', 18)
print(person.first)
print(person.last, person.age, sep="\n")
print(person.full_name())
# 修改属性  同字典一样的操作

# 在类中添加字典作为成员
d = {'dogs': 5, 'cats': 4}
person.critters = d
print(person.critters)