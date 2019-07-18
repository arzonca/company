from company2 import Task, Salaried, Hourly, Company    #importujemy klasę Task z    tworzymy obiekty klasy Task


def read_tasks_from_file(path):    #czyta plik do listy obiektów tzwl otwarcie nowego kontekstu
    tasks = []
    with open(path) as f:  # otwiera plik i przypisuje ten plik do zmiennej f
        for line in f:
            try:
                line = line.strip()   # wywoła nie linikji z pominieciem enterów (opuszczanie pustych linii), funkcja strip na obieicie line usuwa biały znak konca linii (line = obiekt napis)
                # wynikiem jest line - linijka z pliku
                line = line.split(";")   #dzielimy linie line według ';' i daje zawsze do listy, wynikiem jest line = lista wyrazów
                description = line[0]
                points = int(line[1])
                tasks.append(Task(description, points))
            except Exception:
                print("{} is wrong, Cannot parse!".format(line))
    return tasks


def read_salaried_employees_from_file(path1):
    employees = []
    with open(path1) as f:
        for line in f:
            line = line.strip()
            line = line.split(";")    # lub obie linijki line = line.strip().split(";")
            name = line[0]
            age = int(line[1])
            weekly_salary = int(line[2])
            employees.append(Salaried(name, age, [], weekly_salary))     #[] przekazywana pusta lista tasks
    return employees


def read_hourly_employees_from_file(path2):
    employees = []
    with open(path2) as f:
        for line in f:
            line = line.strip()
            line = line.split(";")
            name = line[0]
            age = int(line[1])
            number_of_hours = int(line[2])
            hourly_salary = int(line[3])
            employees.append(Hourly(name, age, [], number_of_hours, hourly_salary))
    return employees

if __name__ == '__main__':
    # print_lines_in_files('tasks1.txt')
    # lines = read_lines_in_file('tasks1.txt')
    # print(lines)
    tasks = read_tasks_from_file('tasks1.txt')
    salaried_employees = read_salaried_employees_from_file('salaried_employees.txt')
    hourly_employees = read_hourly_employees_from_file('hourly_employees.txt')

    employees = salaried_employees + hourly_employees
    company = Company("AGH", employees, tasks)

    company.print_employees()
    company.distribute(len(tasks))
    company.work_all()
    company.print_employees()
    print(company.employees_salary)






