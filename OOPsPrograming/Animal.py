class Animal:
    def general(self):
        print("general : Animal")

class Dog(Animal):
    def __init__(self):
        self.name = "Dog"

    def specific(self):
        print("Dog barks")

class Horse(Animal):
    def __init__(self):
        self.name = "Horse"

    def specific(self):
        print("Horse runs")

d = Dog()
d.general()
d.specific()
print(d.name)

h = Horse()
h.general()
h.specific()
print(h.name)

a = Animal()
a.general()
print(isinstance(d, Dog), isinstance(h, Horse))
print(issubclass(Dog,Animal), issubclass(Horse, Animal))