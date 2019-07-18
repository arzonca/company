class TooManyTasksToDistributeException(Exception):
    pass


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
            raise TooManyTasksToDistributeException()
        while number > 0:
            employee_index = number % len(self.employees)
            task = self.tasks.pop()
            self.employees[employee_index].add_task(task)
            number -= 1

    def print_employees(self):
        for employee in self.employees:
            print("My name is {} and I have {} tasks and {} points ze zrobionych tasków".format(employee.name, employee.number_of_tasks, employee.sum_of_points_of_done_tasks))
        print()

    def work_all(self):
        for employee in self.employees:
            employee.work()

    @property
    def employees_salary(self):
        return sum([employee.salary for employee in self.employees])

    def write_report(self, path1):
        with open(path1, 'w') as f:
            for employee in self.employees:
                f.write("{}\n".format(employee.description()))     #w zaleznosci od tego, jakiej klasy dziedziczącej z Employee jest dany employee (czy Salaried czy Hourly), funkcjia description wykonuje sie
                # według definicji zapisanej odpowiedniej klasie pasującej od danego employee (jesli jest to employee z Salaried, to descrition z Salaried, jesli employee z kl. Employee, to wg def. z klasy Employee


class Task:
    def __init__(self, description, number_of_points):
        self.description = description
        self.number_of_points = number_of_points
        self.is_done = False

    def execute(self):
        self.is_done = True

class Employee:
    def __init__(self, name, age, tasks):     # tasks - zadania do wykonania
        self.name = name
        self.age = age
        self.tasks = tasks

    def description(self):
        return "My name is {} and I am {} years old".format(self.name, self.age)

    def work(self):
        not_done_tasks = [task for task in self.tasks if not task.is_done]
        if len(not_done_tasks) > 0:
            not_done_tasks[0].execute()

    def add_task(self, task):
        self.tasks.append(task)  # tu efektem jest czynnosci dodania, dlatego nie ma return

    @property
    def sum_of_points_of_done_tasks(self):
        return sum([task.number_of_points for task in self.tasks if task.is_done])

    @property
    def salary(self):
        raise NotImplementedError()

    @property
    def number_of_tasks(self):
        return len(self.tasks)   # tu zwracamy liczbę


class Salaried(Employee):
    def __init__(self, name, age, tasks, weekly_salary):
        super().__init__(name, age, tasks)
        self.weekly_salary = weekly_salary

    @property        # dla propoerty nie musi byc nawiasów przy wywołaniu
    def salary(self):
        return 4 * self.weekly_salary

    def description(self):
        return "{} and I earn {} monthly.".format(super().description(), self.salary)


class Hourly(Employee):
    def __init__(self, name, age, tasks, number_of_hours, hourly_salary):
        super().__init__(name, age, tasks)
        self.number_of_hours = number_of_hours
        self.hourly_salary = hourly_salary

    @property
    def salary(self):
        return self.number_of_hours * self.hourly_salary

    def description(self):
        return "{} and I earn {} monthly.".format(super().description(), self.salary)



if __name__ == "__main__":

    number_of_hours = 168

    tasks = [Task("Zadanie 1", 10), Task("Zadanie 2", 10), Task("Zadanie 3", 10), Task("Zadanie 4", 10)]

    employees = [Salaried("Tomasz", 34, [], 2000), Salaried("Antoni", 34, [], 2000), Hourly("Maciej", 44, [], 50, 2500), Hourly("Zenek", 41, [], 20, 3000)]

    company = Company("AGH", employees, tasks)

    company.print_employees()
    print()
    company.distribute(4)
    for employee in employees:
        employee.work()
        company.print_employees()
        print()

    # company.print_employees()
    # company.distribute(3)
    # print()
    # company.print_employees()
    #
    # company.employees[1].work()
    #
    # print()
    # company.print_employees()
    # print()
    # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    # print()
    try:
        company.distribute(10)
    except TooManyTasksToDistributeException:
        print("You entered too many tasks to distribute.")

    company.write_report('report.txt')