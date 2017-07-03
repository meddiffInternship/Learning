class Employee:
    raise_amt = 1.04
    emp_count = 0

    def __init__(self, name, salary, age, empid):
        self.name = name
        self.salary = salary
        self.age = age
        self.empid = empid
        Employee.emp_count += 1

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

    def displayEmployee(self):
        print('Name: ', self.name ,'\n','Salary: ',self.salary,
              '\n','Age: ',self.age)


emp1 = Employee('Anupama', 15000, 14, 1001)
emp2 = Employee('Anarghya', 20000, 23, 2001)

print(Employee.emp_count)

print(Employee.raise_amt)
print('---------------------------------------------')
print(emp1.__dict__)
print('---------------------------------------------')
print(Employee.__dict__)

emp1.raise_amt=1.05
print('---------------------------------------------')
print(Employee.raise_amt)
print(emp1.raise_amt)
print('---------------------------------------------')
print(emp1.__dict__)


