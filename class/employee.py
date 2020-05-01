class Employee:

    num_of_emps = 0
    amount_raise = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

        Employee.num_of_emps += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.salary = int(self.salary*self.amount_raise)


emp_1 = Employee('Monica', 'Maibram', 50000)
emp_2 = Employee('Test', 'User', 50000)

print(Employee.num_of_emps)
emp_1.amount_raise = 1.05
emp_1.apply_raise()
print(emp_1.salary)

emp_2.apply_raise()
print(emp_2.salary)
