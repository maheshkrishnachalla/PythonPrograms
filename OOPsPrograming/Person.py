class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def person_details(self):
        print("{} is {} years from {} ".format(self.name, self.age, self.address))


def main():
    person1 = Person("Ganesh", 27, "Hyderabad")
    person2 = Person("Saroja", 24, "Chennai")
    person1.person_details()
    person2.person_details()

if __name__ == '__main__':
    main()
