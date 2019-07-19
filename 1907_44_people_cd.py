class Person:
    def __init__(self, name):
        self.name = name

    @property
    def description(self):
        return "I am Person. My name is {}.".format(self.name)


class Student(Person):
    def __init__(self, name):
        super().__init__(name)


class Doctor(Person):
    def __init__(self, name, salary):
        super().__init__(name)       # w tym miesiecy jest jakby Person(self.name = name)
        self.salary = salary

    @property
    def description(self):
        return "I am a Doctor. My name is {}.".format(self.name)



def g(person):   #7
    new_person = person    #8
    person = None   #9
    person = Student("Kamil")    #10
    person.name = "Wojciech"    #11
    new_person.name = "Natalia"    #12

if __name__ =='__main__':
    p1 = Student("Piotr")  #1, str.10a
    p2 = Doctor("Ewa", 5000) #2
    p3 = Student("Marysia") #3

    p3 = p2  #4
    p2 = p1 #5
    p3 = p2 #6
    g(p3)

    print(p1.name)
    print(p2.name)


