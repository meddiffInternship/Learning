class Employee:
    raise_amount = input('The appraisal amount?')
    

    
    def __init__(self,empName,empSal):

        self.empName=empName
        self.empSal=empSal
        self.empEmail=self.empName +'@company.com'
        self.empSal_rise=int(self.empSal)*int(Employee.raise_amount)



    '''def apply_raise(self):
        self.empSal_rise=self.empSal*Employee.raise_amount'''

name=input('enter the name of the employee')
salary=input('enter the salary of the employee')
emp1= Employee(name,salary)
        

print(emp1)
print(emp1.empEmail)
#emp1.apply_raise()
print(emp1.empSal_rise)




        

        
        
