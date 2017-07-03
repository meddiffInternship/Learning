
class Student:

    def __init__(self, rollno, first, last, sem):
        self.rollno = rollno
        self.first = first
        self.last = last
        self.sem = sem

    def display_details(self):
        return 'Roll No: {} \n Full Name: {} {} \n Semester: {}'.format(self.rollno,
                                             self.first, self.last, self.sem)

class Marks(Student):

    def __init__(self, rollno, first, last, sem, sub1, sub2):
        super().__init__(rollno, first, last, sem)
        self.sub1 = sub1
        self.sub2 = sub2

    def sub_marks(self):
        self.total = (self.sub1 + self.sub2)/2
        return self.total

class sports():

    def __init__(self, sport):
        self.sport = sport

    def sportsMarks(self):
        if self.sport == 'Gymnastics':
            return 5
        elif self.sport == 'Chess':
            return 4
        elif self.sport == 'Swimming':
            return 3

class Final_grade(Marks, sports):
    
    def __init__(self, rollno, first, last, sem, sub1, sub2, sport):
        Marks.__init__(self, rollno, first, last, sem, sub1, sub2)
        sports.__init__(self, sport)

    def grade(self):
        self.tot = int(self.sub_marks()) + int(self.sportsMarks())
        if self.tot >= 75:
            return 'A'
        elif self.tot < 75 and self.tot >= 60:
            return 'B'
        elif self.tot < 60 and self.tot >= 40:
            return 'C'
        else:
            return 'F'

std1 = Final_grade(12, 'Zoro', 'Roronoa', 3, 90, 80, 'Swimming')
print(std1.display_details())
print(std1.grade())
print(std1.tot)
        

    

    
