base = {'IT': 260,
        "MED": 240,
        'Engenir' : 219}

class Student():
    def __init__(self,name,degree,facult,scoreEGE = 0):
        self.__init__(name)
        self.degree = degree
        self.facult = facult
        self.scoreEGE = scoreEGE
    def display(self):
        print(self.name,self.facult,self.degree,self.scoreEGE)
class Abitu(Student):
    def __init__(self):


class EGE():
    def __init__(self,subj,score):
        self.subj = subj

    # def test(self,score):
    #     self.score = int(input('ur total score on EGE:'))
    #     return self.score
class Vyz():
    def __init__(self,name):
        self.name = name
        self.facs_and_scores = {}
        self.prosh={}
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
            prosh[student.facult].append(student.name)
        else:
            print('no')
if __name__ =='__main__':

    vlad = Student('Vlad',1,'IT',250)
    vlad.display()
    MIIT = Vyz('MIIT')
    MIIT.new_fac('Engeniring',249)
    MIIT.new_fac('IT',257)
    MIIT.new_fac('LOGIST',180)
    MIIT.display_info()
    vlad = Student('vlad',1,'IT',280)
    MIIT.priem_v_vyz(vlad)


