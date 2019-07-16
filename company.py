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


    def description(self):
        return "My name is {} and I am {} years old.".format(self.name, self.age)


    def work(self):
        not_done_tasks = [task for task in self.tasks if not task.is_done]   #zrobienie listy niezrobionych tasków: umieśc na liscie nowy task, sprawdzając poprzez każde zadanie task
        # na liscie Tasks, czy jest niewykonane czyli czy pole is_done dla taska nie jest true  - 'if not task.is_done' równoznaczne z 'if task.is_done == False')
        if not_done_tasks:  #jeśli długość tej listy jest rózna od zera
            not_done_tasks[0].execute()   # znajdujemy pierwsze niewykonane zadanie i je zmieniamy na True, wiec jest wykonane


    def add_task(self, task):
        self.tasks.append(task)  #na liscie tasks dodaj task


    @property
    def points_of_done_tasks(self):
        return [task.number_of_points for task in self.tasks if task.is_done] #wypełnienie listy ilosci punktów za wykonane zadania

    @property
    def salary(self):
        raise NotImplementedError()



class Salaried(Employee):
    def __init__(self, name, age, tasks, weekly_salary):
        super().__init__(name, age, tasks)
        self.weekly_salary = weekly_salary


    @property
    def salary(self):
        return 4*self.weekly_salary

    def description(self):
        return "{} and I earn $ {} per month.".format(super().description(), self.salary())



class Hourly_paid(Employee):
    def __init__(self, name, age, tasks, hours_weekly, per_hour):
        super().__init__(name, age, tasks)
        self.hours_weekly = hours_weekly
        self.per_hour = per_hour

    @property
    def salary(self):
        return 168 * self.hours_weekly


    def description(self):
        return "{} and I earn $ {} per month.".format(super().description(), self.salary())



if __name__ == "__main__":
    task1 = Task("Zadanie pierwsze", 10)
    task2 = Task("Zadanie pierwsze", 20)
    task3 = Task("Zadanie pierwsze", 30)
    task4 = Task("Zadanie pierwsze", 40)
    task5 = Task("Zadanie pierwsze", 50)

    employee1 = Employee("Tomasz", 34, )
    employee2 = Employee("Maciej", 44, )

    salaried = Salaried()