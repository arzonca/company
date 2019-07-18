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

    # def f1(person):
    #     person.name = "Marcin"
    #
    #
    # def f2(person):
    #     person.name = "Marcin"
    #     person = None

    def f3(person):
        person = Student("Ignacy")
        person.name = "Marcin"


class Professor:
    def __init__(self, students):
        self.students = students

def f(person):
    new_person = person
    person = Student("Ignacy")
    new_person.name = "Marcin"

if __name__ == '__main__':

    p1 = Student("Piotr")
    p2 = Doktor("Ewa", 5000)

    p2 = p1
    f(p1)
    print(p1.name)
    print(p2.name)





    # student_list = [Student("Piotr"), Student("Ewa")]
    # professor = Professor(student_list)
    #
    # student_list = [1, 2, 3]
    # print(student_list)
    # print(professor.students)

    # person_1 = Person("Piotr")  #tworzy sie zmienna person i do niej przypisano atrybut z obiektu Person
    # person_2 = Student("Ewa")
    # person_3 = Doktor("Maciej", 10000)

    # person_2 = person_3
    # print(person_2.name)   #p2 wskazuje na to samo, na co p3, a p3 wskazuje na Macieja
    # print(person_3.name)

    # person_2 = person_3
    # person_3.name = "Piotr"
    # print(person_2.name)   #p2 wskazuje na to samo, na co p3, a p3.name jest podmienione na Poitr
    # print(person_3.name)

    # person_2 = person_3
    # person_3.name = "Piotr"
    # person_3 = Doktor("Tomasza", 5000)
    # print(person_2.name)   #p2 wskazuje na to samo, na co p3, a p3.name jest podmienione na Poitr, a potem oba pola w p3 sa podmienione na Tomasza i 5000, w wskazane dla p2 piotr zostaje
    # print(person_3.name)

    # person_2 = person_3
    # f1(person_3)
    # print(person_2.name)  # p2 wskazuje na to samo, na co p3, a funkcja zmienia name na Marcin, wynik 2 x Marcin
    # print(person_3.name)
    #
    # person_2 = person_3
    # f1(person_3)
    # print(person_2.name)  # p2 wskazuje na to samo, na co p3, a funkcja zmienia name na Marcin
    # print(person_3.name)
    #
    # person_2 = person_3
    # f2(person_3)
    # print(person_2.name)  # p2 wskazuje na to samo, na co p3, a funkcja zmienia name na Marcin, None
    # print(person_3.name)

    # person_2 = person_3   #ucina połaczniee Ewa znika
    # f3(person_3)            #tworzymy czwaety obiekt Student("Ignacy"), ucinanane jest połaczenie miedzy person a doktorem Maciejem
    # print(person_2.name)  # p2 wskazuje na to samo, na co p3, a funkcja zmienia name na Marcin, None
    # print(person_3.name)

