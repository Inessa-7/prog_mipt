class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return " ".join(map(str, self.__dict__.values()))


class Zebra(Animal):
    def __init__(self, name, age, country):
        super().__init__(name, age)
        self.country = country


class Dolphin(Animal):
    def __init__(self, name, age, ocean):
        super().__init__(name, age)
        self.ocean = ocean


z = Zebra('Marty', 12, 'Africa')
d = Dolphin('aaa', 13, 'Pacific')
print(z)
print(d)
