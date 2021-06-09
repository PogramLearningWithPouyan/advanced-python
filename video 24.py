class user:
    def __init__(self,name,age):
        self.name=name
        if age>0:
            self._age=age
        else:
            self._age=0

    #def get_age(self):
       # return self._age
    @property
    def age(self):
        return self._age

    #def set_age(self,value):
        #if value>0:
            #self._age=value
    @age.setter
    def age(self,value):
        if value>0:
            self._age=value
    @property
    def fullName(self):
        return f'{self.name} is {self._age}'

me=user('pouyan',30)
print(me.age)
me.age=12
print(me.age)
print(me.fullName)