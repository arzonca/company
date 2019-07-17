class TooManyTasksToDistributeException(Exception):
    pass


class Task:
    def __init__(self, text, number_of_points):
        self.text = text
        self.number_of_points = number_of_points
        self.is_done = False

    def execute(self):
        self.is_done = True   #modyfikuje pole is_done


class Employee:
    def __init__(self, name, age, tasks):
        self.name = name
        self.age = age
        self.tasks = tasks


  #  def description(self):
   #     return "My name is {} and I am {} years old.".format(self.name, self.age)


    def work(self):
        not_done_tasks = [task for task in self.tasks if not task.is_done]   #zrobienie listy niezrobionych tasków: umieśc na liscie nowy task, sprawdzając poprzez każde zadanie task
        # na liscie Tasks, czy jest niewykonane czyli czy pole is_done dla taska nie jest true  - 'if not task.is_done' równoznaczne z 'if task.is_done == False')
        if not_done_tasks:  #jeśli długość tej listy jest rózna od zera
            not_done_tasks[0].execute()   # znajdujemy pierwsze niewykonane zadanie i je zmieniamy na True, wiec jest wykonane


    def add_task(self, task):
        self.tasks.append(task)  #na liscie tasks dodaj task


    @property
    def sum_of_points_of_done_tasks(self):
        return sum([task.number_of_points for task in self.tasks if task.is_done]) #wyliczenie sumy leentów listy ilosci punktów za wykonane zadania

    @property
    def salary(self):
        raise NotImplementedError()

    @property
    def number_of_tasks(self):
        return len(self.tasks)



class Salaried(Employee):
    def __init__(self, name, age, tasks, weekly_salary):
        super().__init__(name, age, tasks)
        self.weekly_salary = weekly_salary


    @property
    def salary(self):
        return 4*self.weekly_salary

    def description(self):
        return "{} and I earn $ {} per month.".format(super().description(), self.salary)



class Hourly_paid(Employee):
    def __init__(self, name, age, tasks, hours_weekly, per_hour):
        super().__init__(name, age, tasks)
        self.hours_weekly = hours_weekly
        self.per_hour = per_hour

    @property
    def salary(self):
        return 168 * self.hours_weekly


    def description(self):
        return "{} and I earn $ {} per month.".format(super().description(), self.salary)


class Company:
    def __init__(self, name, employees, tasks):
        self.name = name
        self.employees = employees
        self.tasks = tasks

    def add_employee(self, employee):
        self.employees.append(employee)


    def add_task(self, task):
        self.tasks.append(task)


    def distribute(self, number):
        if number > len(self.tasks):
            raise TooManyTasksToDistributeException()     #podnosimy wyjątek, jesli ilośc tasków, które chcemy przydzielic do wykonaia jest wieksza niz ilośc tasków
        while number > 0:    #po ilości taskow do wykonania
            employee_index = number % len(self.employees)
            task = self.tasks.pop() #usuwanie kolejnych tasków z listy tasks
            self.employees[employee_index].add_task(task)      #self.employees[empolyee_index]  - zwraca pracownika znajdującego się pod [] na liscie pracowników
            # na tym pracowniku uruchamiamy funkcje dodania taska z listy tasks
            number -= 1
            #lub

            #self.employees[number % len(self.employees)].add_task(self.tasks.pop()]

    def print_employees(self):
        for employee in self.employees:
            print('My name is {} and I have {} tasks and {} points ze zrobionych tasków'.format(employee.name, employee.number_of_tasks, employee.sum_of_points_of_done_tasks))
            # lepiej to len(employee.tasks) zamienic property w klasie Employee



if __name__ == "__main__":

    tasks = [Task("Zadanie 1", 10), Task("Zadanie 2", 20), Task("Zadanie 3", 30), Task("Zadanie 4", 40) ]

    employees = [Salaried("Tomasz", 34, [], 2000), Hourly_paid("Maciej", 44, [], 50, 5)]

    company = Company("AGH", employees, tasks)

    # for employee in employees:
    #     print(employee.sum_of_points_of_done_tasks)                                     #ile punktów aktualnie maja pracownicy
    #
    # for employee in employees: # for #niech kazdy pracownik wykona jedno zadanie (work)
    #     employee.work()
    #
    # for employee in employees:
    #     print(employee.sum_of_points_of_done_tasks)

    # for employee in employees:
      #  print("Liczba tasków pracownika {} wynosi {}".format(employee.name, len(employee.tasks)))

    company.print_employees()
    company.distribute(3)
    print()
    company.print_employees()

    company.employees[0].work()

    print()
    company.print_employees()

    try:
        company.distribute(10)
    except TooManyTasksToDistributeException:
        print("You entered too many tasks to distribute.")
