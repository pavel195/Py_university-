base = {'IT': 260,
        "MED": 240,
        'Engenir' : 219}
class Student:
    def __init__(self,name,degree,facult,scoreEGE):
        self.degree = degree
        self.facult = facult
        self.scoreEGE = scoreEGE

class Vyz():
    def __init__(self,facs,scores):
        self.facs = facs
        self.scores = scores
facs = ['IT','MED',"ENG"]

class priem_v_vyz(Vyz):





egor = Vyz('egor',1,'IT',215)
vlad = Vyz('vlad',1,'MED',280)





# class Vyz(Student):
#     def __init__(self,name,degree,facult,scoreEGE):
#         super().__init__(name,degree,facult,scoreEGE)
#     def priem_v_vyz(self):
#         if self.scoreEGE >= base[self.facult]:
#             print(f'UR are hired! u have {self.scoreEGE}, but u need {base[self.facult]}')
#         else:
#             print(f'SORYY,take a chance next year!U have {self.scoreEGE}, but u need {base[self.facult]}')
# egor = Vyz('egor',1,'IT',215)
# vlad = Vyz('vlad',1,'MED',280)
# egor.priem_v_vyz()
# vlad.priem_v_vyz()

