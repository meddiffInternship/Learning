class Student:

    def __init__(self, rollno, first, last, sem):
        self.rollno = rollno
        self.first = first
        self.last = last
        self.sem = sem

    
    @property
    def display_details(self):
        return 'Roll No: {} \n Full Name: {} {} \n Semester: {}'.format(self.rollno,
                                             self.first, self.last, self.sem)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

class Marks(Student):

    def __init__(self, rollno, first, last, sem, sub1, sub2):
        super().__init__(rollno, first, last, sem)
        self.sub1 = sub1
        self.sub2 = sub2

    def sub_marks(self):
        self.total = (self.sub1 + self.sub2)/2
        return self.total

s1 = Marks(19, 'Trafalgar', 'Law', 5, 60, 80)
print(s1.sub_marks())
s1.fullname = 'Sanji Vinsmoke'
print(s1.fullname)
print(s1.display_details)
