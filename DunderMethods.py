class Student:

    def __init__(self, rollno, first, last, sem, sub):
        self.rollno = rollno
        self.first = first
        self.last = last
        self.sem = sem
        self.sub = sub

    def display_details(self):
        return 'Roll No: {} \n Full Name: {} {} \n Semester: {}'.format(self.rollno,
                                             self.first, self.last, self.sem)

    def __repr__(self):
        return 'Printing from __repr__() \nRoll No: {} \nFull Name: {} {} \nSemester: {}'.format(self.rollno,
                                             self.first, self.last, self.sem)

    def __str__(self):
        return 'Printing from __str__() \nFull Name: {} {} \nMarks: {}'.format(self.first,
                                                         self.last, self.sub)

    def __add__(self, other):
        return self.sub + other.sub

s1 = Student(25, 'Trafalgar', 'Law', 5, 80)
s2 = Student(19, 'Zoro', 'Roronoa', 5, 40)
print(s1 + s2)
print('---------------------------------------------------')
print(s2.__repr__())
print('---------------------------------------------------')
print(s1)
