
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, sal):
        self.first = first
        self.last = last
        self.sal = sal
        self.email = first + '.' +  last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def salary_raise(self):
        self.sal = int(self.sal * self.raise_amt)

class Developer(Employee):

    def __init__(self, first, last, sal, lang):
        super().__init__(first, last, sal)
        self.lang = lang

class Manager(Employee):
    def __init__(self, first, last, sal, emp_list=None):
        super().__init__(first, last, sal)
        if emp_list == None:
            self.emp_list = []
        else:
            self.emp_list = emp_list

    def add_emp(self, emp):
        if emp not in self.emp_list:
            self.emp_list.append(emp)

    def remove_emp(self, emp):
        if emp in self.emp_list:
            self.emp_list.remove(emp)

    def print_emp(self):
        for emp in self.emp_list:
            print(emp.fullname())

dev1 = Developer('Trafalgar', 'Law', 25000, 'Java')
dev2 = Developer('Zoro', 'Roronoa', 30000, 'Python')

mng1 = Manager('Luffy', 'Monkey', 50000, [dev1])
mng1.add_emp(dev2)
mng1.remove_emp(dev2)

mng1.print_emp()
print(mng1.email)

print(isinstance(mng1, Developer))
print(issubclass(Manager, Employee))









    
            
        
    
