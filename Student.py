base = {'IT': 260,
        "MED": 240,
        'Engenir' : 219}
class Person:
    def __init__(self,name):
        self.name = name
class Student(Person):
    def __init__(self,name,degree,facult,scoreEGE):
        super().__init__(name)
        self.degree = degree
        self.facult = facult
        self.scoreEGE = scoreEGE
    def display(self):
        print(self.name,self.facult,self.degree,self.scoreEGE)
vlad = Student('Vlad',1,'IT',250)
vlad.display()
class EGE():
    def s(self):
        self.score = int(input('ur total score on EGE:'))
class Vyz():
    def __init__(self,name):
        self.name = name
        self.facs_and_scores = {}
    def display_info(self):
        print(self.name,self.facs_and_scores)
    def new_fac(self,fac,score):
        # self.fac = input('name of facultet:')
        # self.score = int('score for facult:')
        self.fac = fac
        self.score = score
        self.facs_and_scores[self.fac] = self.score
    def priem_v_vyz(self,student):
        if student.scoreEGE >= self.facs_and_scores[student.facult]:
            print('u are hired')
        else:
            print('no')
MIIT = Vyz('MIIT')
MIIT.new_fac('Engeniring',249)
MIIT.new_fac('IT',257)
MIIT.new_fac('LOGIST',180)
MIIT.display_info()
vlad = Student('vlad',1,'IT',280)
MIIT.priem_v_vyz(vlad)


