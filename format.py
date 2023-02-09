class Person:
    def __init__(self,name , age ):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Name: %s, age : %d' %(self.name, self.age) +'\n' + \
               'Name : {0.name} and age: {0.age}'.format(self) + '\n' + \
               f'Name: {self.name}, age : {self.age *2 }'


Vasya = Person('Vasya', 39)
print(Vasya)
