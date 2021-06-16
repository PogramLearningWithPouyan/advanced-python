class person:
    def __init__(self,name,family):
        self.name=name
        self.family=family
    @property
    def fullName(self):
        return f"{self.name} {self.family}"
class user(person):
    def __init__(self,name,family,email):
        #person.__init__(self,name,family)
        super().__init__(name,family)
        self.email=email

pouyan=user('pouyan','rajian','test@test.com')
#ali=person()
print(pouyan.fullName)