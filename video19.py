#_name
#__name => name mangeling
#__name__

class user:
    def __init__(self,name,email,password):
        self.username=name
        self._email=email
        self._password=password
        self.__ID=23
    def login(self,getpassword):
        if getpassword== self._password:
            print('login')
        else:
            print('wrong password')

class new:
    def __init__(self):
        self.__ID=00

me=user('pouyan','test@gmail.com',123)
you=new()
print(me._user__ID)
print(you._new__ID)

me.login(123)
