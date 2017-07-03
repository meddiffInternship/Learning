
# coding: utf-8

# # oops !

# In[ ]:

#class concept


# In[ ]:

class Meddiff:
    def __init__(self,name,department):
        self.name = name
        self.department = department
    def display(self):
        print("the name is",self.name)
        print("the department",self.department)

if __name__ == '__main__':
    med = Meddiff("aayushi","analytics")
    med.display()


# # class variables 

# In[43]:

class Area:
    pi = 3.14
    def Square(self,a):
        self.side = a
        self.area =  4*self.side
        print('The area is ',self.area)
    def circle(self,r):
        self.radius = r
        self.a = self.pi*self.radius*self.radius
        print('th area of circle is',self.a)
    def main():
            ar = Area()
            #print(ar.pi)
            print(ar.__dict__)
            ar.Square(10)
            ar.circle(2)
Area.main()
#print(Area.pi)
print(Area.__dict__)


# In[ ]:

#object


# In[17]:

#simple class
class University:
    raise_fees = 1.04
    def Accounts(self,fees,adm_no):
        self.payment = fees
        self.reference = adm_no
       
    def Teacher(self,classes,subject):
        self.class_sec = classes
        self.sub_taught = subject
    def display(self):
        print( str(self.payment) +"," +self.reference)
        print( str(self.class_sec) +","+ self.sub_taught)
    @classmethod
    def raise_fee_amt(cls,pay):
        cls.raise_fees = pay
        
print(University.raise_fees)
#University.raise_fee_amt(1.05)
#running class method from class 
print(University.raise_fees)
u = University()
#running class method from instance
u.raise_fee_amt(1.06)
print(u.raise_fees)
#u.Accounts(30000,'mit/124')
#u.Teacher('bda','python')
#u.display()
#print(u)






# # Inheritance

# In[48]:

#simple inheritance
class University:
    raise_fees = 1.04
    num_of_studs = 40
    def Accounts(self,fees,adm_no):
        self.payment = fees
        self.reference = adm_no
        University.num_of_studs+=1
    def Teacher(self,classes,subject):
        self.class_sec = classes
        self.sub_taught = subject
    def display(self):
        print( str(self.payment) +"," +self.reference)
        print( str(self.class_sec) +","+ self.sub_taught)
    @classmethod
    def raise_fee_amt(cls,pay):
        cls.raise_fees = pay
class student(University):
    def display_details(self):
        self.display()
        
#class variable without using self 
print(University.num_of_studs)
print(University.raise_fee_amt)
u = University()
s = student()
s.Accounts(158000,'mit/123')
s.Teacher('Msc','PSI')
s.display_details()
#print(University.num_of_studs)

#print(isinstance(u,student))
#print(issubclass(student,University))


# In[ ]:

class University:
    def Accounts(self,fees,adm_no):
        self.payment = fees
        self.reference = adm_no
    def Teacher(self,classes,subject):
        self.class_sec = classes
        self.sub_taught = subject
    def display(self):
        print( str(self.payment) +"," +self.reference)
        print( str(self.class_sec) +","+ self.sub_taught)

class student(University):
    def fees_payment(self,fees,adm_no,status):
        University.Accounts(self,fees,adm_no)
        self.stat = status
    def Stud_details(self,classes,subject,students):
        University.Teacher(self,classes,subject)
        self.stud = students 
    def display_details(self):
        print(str(self.display()) +","+ str(self.stud))
        print(str(self.display()) +","+ self.stat)
u = University()
s = student()
u.Accounts(158000,'mit/123')
u.Teacher('MSc','PSI')
s.fees_payment(158000,'mit/123','not yet')
s.Stud_details('MSc','PSI',40)
#u.display()
s.display_details()
    


# In[ ]:

#inheriting from multiple parent class
class University:
    def Accounts(self,fees,adm_no):
        self.payment = fees
        self.reference = adm_no
    def Teacher(self,classes,subject):
        self.class_sec = classes
        self.sub_taught = subject
    def display(self):
        print( str(self.payment) +"," +self.reference)
        print( str(self.class_sec) +","+ self.sub_taught)
class Department:
    def dept(self,dept_id,dept_name):
        self.dept_ref = dept_id
        self.department = dept_name
    def dept_details(self):
        print(str(self.dept_ref)+""+self.department) 
        
          

class student(University,Department):
    def display_details(self):
        self.display()
        self.dept_details()
        



s = student()
s.Accounts(158000,'mit/123')
s.Teacher('Msc','PSI')
s.dept(101,'stats')
s.display_details()
s.dept_details()



# In[1]:

#simple inheritance
class School:
    def Accounts(self):
        self.fees = input("enter fees")
        self.adm_no = input("enter id")
    def Teacher(self):
        self.class_sec = input("enter sec")
        self.sub_taught = input("enter the subject")
    def display(self):
        print( str(self.fees) +"," +self.adm_no)
        print( str(self.class_sec) +","+ self.sub_taught)
class Student:
    def add_details(self):
        self.rollno = input("enter rollno")
        self.Name = input("enter student  name")
        self.Parentname = input("enter parents's name")
    def stud_details(self):
        print(str(self.rollno)+","+self.Name+","+self.Parentname)
        
        
class records(School,Student):
    def display_details(self):
        self.display()
        self.stud_details()
        
        



r = records()
r.Accounts()
r.Teacher()
r.add_details()
r.display_details()




# # Overriding methods

# In[31]:

class Add:
    def addition(self):
        self.num2 = input("enter first number")
        self.num3 = input("enter second num")
        self.num1 = int(self.num2 )+ int(self.num3)
        print(self.num1)
class show(Add):
    def addition(self):
        self.num1 = input("enter ")
        self.num2 = input("enter first number")
        self.num3 = int(self.num1) * int(self.num2)
        print(self.num3)

s = show()
s.addition()
        

