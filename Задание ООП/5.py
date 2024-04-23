class Employee:
    def __init__(self, salary):
        self.salary = salary

    def get_paid(self):
        print(self.salary)


class Manager(Employee):
    pass


class Worker(Employee):
    pass


manager_paid = Manager(50000)
worker_paid = Worker(35000)

manager_paid.get_paid()
print(type(manager_paid))
worker_paid.get_paid()
print(type(worker_paid))
