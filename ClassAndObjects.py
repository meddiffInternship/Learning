class Employee:
    emp_count = 0

    def __init__(self, name, salary, age, empid):
        self.name = name
        self.salary = salary
        self.age = age
        self.empid = empid
        Employee.emp_count += 1

    def displayCount(self):
        print('Total number of employee: {}'.format(Employee.emp_count))

    def displayEmployee(self):
        print('Name: ', self.name ,'\n','Salary: ',self.salary,
              '\n','Age: ',self.age)


emp1 = Employee('Anupama', 15000, 14, 1001)
emp2 = Employee('Anarghya', 20000, 23, 2001)
emp1.displayEmployee()
emp2.displayEmployee()
emp2.displayCount()

print(getattr(emp1, 'empid'))

if hasattr(emp1, 'age'):
    setattr(emp1, 'age', 23)
    emp1.displayEmployee()
else:
    print('Attribute does not exist')

delattr(emp1, 'empid')

if hasattr(emp1, 'empid') == False:
    print('Attribute deleted')

#Basic class attributes

print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)
print(Employee.__dict__)
