class person:
    def __init__(self,name):
        print('in person')
        self.name=name
    def sayhello(self):
        return f'hello {self.name} in person'
    def saybye(self):
        return f'good bye {self.name}'
class user:
    def __init__(self,name):
        print('in user')
        self.name=name
    def sayhello(self):
        return f'hello {self.name} in user'
    def sayok(self):
        return f'you are okey {self.name}'
class admin(person,user):
    def __init__(self,name):
        print('in admin')
        #super().__init__(name)
        person.__init__(self, name)
        user.__init__(self,name)


#person1=admin('pouyan')
#print(person1.saybye())
# print(isinstance(person1,admin))
# print(isinstance(person1,person))
# print(isinstance(person1,user))

#method resolution order
#__mro__
#mro()
#help(cls)

# print(admin.__mro__)
# print(admin.mro())
# print(help(admin))
class a:
    def sayhello(self):
        print('hello in a')\

class b(a):
    pass
    # def sayhello(self):
    #     print('hello in b')

class c(a):
    pass
    # def sayhello(self):
    #     print('hello in c')

class d(c,b):
    pass
    # def sayhello(self):
    #     print('hello in d')

x=d()
#x.sayhello()
print(help(d))