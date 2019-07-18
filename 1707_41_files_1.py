from company2 import Task, Salaried     #importujemy klasę Task z    tworzymy obiekty klasy Task


def read_tasks_from_file(path):    #czyta plik do listy obiektów tzwl otwarcie nowego kontekstu
    tasks = []
    with open(path) as f:  # otwiera plik i przypisuje ten plik do zmiennej f
        for line in f:
            line = line.strip()   # wywoła nie linikji z pominieciem enterów (opuszczanie pustych linii), funkcja strip na obieicie line usuwa biały znak konca linii (line to obiekt napis)
            line = line.split(";")   #dzielimy linie line według ';' i daje zawsze do listy
            description = line[0]
            points = int(line[1])
            tasks.append(Task(description, points))
    return tasks


def read_salaried_employees_from_file(path1):
    employees = []
    with open(path1) as g:
        for line in g:
            line = line.strip()
            line = line.split(";")
            name = line[0]
            age = int(line[1])
            weekly_salary = int(line[2])
            employees.append(Salaried(name, age, [], weekly_salary))     #[] przekazywana pusta lista
    return employees




if __name__ == '__main__':
    # print_lines_in_files('tasks1.txt')
    # lines = read_lines_in_file('tasks1.txt')
    # print(lines)
    print(read_tasks_from_file('tasks1.txt'))
    print(read_salaried_employees_from_file('salaried_employees.txt'))





