class person:
    test=123
    def __init__(self,name,family,age):
        self.name=name
        self.family=family
        self.age=age
    def showFullName(self):
        return f'{self.name} {self.family} is {self.age}'

class teacher(person):
    pass


pouyan=person('pouyan','rajian',30)
print(pouyan.showFullName())
ali=teacher('ali','ghafori',26)
print(ali.showFullName())