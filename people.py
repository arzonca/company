class Person:
    def __init__(self, name):
        self.name = name

    @property
    def description(self):
        return "I am Person. My name is {}.".format(self.name)


class Student(Person):
    def __init__(self, name):
        super().__init__(name)


class Doktor(Person):
    def __init__(self, name, salary):
        super().__init__(name)       # w tym miesiecy jest jakby Person(self.name = name)
        self.salary = salary

    @property
    def description(self):
        return "I am a Doctor. My name is {}.".format(self.name)


if __name__== '__main__':
    person_1 = Person("Antoni")  #tworzy sie zmienna person i do niej przypisano atrybut z obiektu Person
    person_2 = Student("Ewa")
    person_3 = Doktor("Zenon", 1000)
    print(person_1.name)
    print(person_1.description)
    print()
    print(person_2.name)
    print(person_2.description)  #dziedziczymy description z klasy wyżej Person
    print()
    print(person_3.name)
    print(person_3.description)
    print()
    person_list = [person_1, person_2, person_3]
    for person in person_list:
        print(person.description)

