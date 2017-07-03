import datetime

class Employee:
    raise_amt = 1.04
    emp_count = 0

    def __init__(self, fname, lname, salary, age, empid):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.age = age
        self.empid = empid
        Employee.emp_count += 1

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

    def display(self):
        print('First Name: ', self.fname ,'\n', 'Last name: ', self.lname, '\n', 'Salary: ',self.salary,
              '\n','Age: ',self.age, '\n', 'Employee ID: ', self.empid)

    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amt = amt

    @classmethod
    def from_string(cls, emp_str):
        fname, lname, sal , age, empid= emp_str.split('-')
        return cls(fname, lname, sal, age, empid)

     #STATIC METHOD
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Anupama', 'Shastry', 15000, 14, 1001)
emp2 = Employee('Anarghya', 'Kini', 20000, 23, 2001)

emp_str_1 = 'Aayushi-Gupta-25000-26-3001'
emp_str_2 = 'Indu-Mathi-18000-23-4001'

new_emp1 = Employee.from_string(emp_str_1)

new_emp1.display()


my_date = datetime.date(2017, 8, 14)

print(Employee.is_workday(my_date))
