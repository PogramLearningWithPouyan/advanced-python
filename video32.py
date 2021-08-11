class user:
    activeUser=[]
    def __init__(self,name,age):
        self.name=name
        self.age=age
        userdict={'name':name,'age':age}
        user.activeUser.append(userdict)
        self.index=0
    def logout(self):
        print(f'{self.name} is logout')
        currentuser=list(filter(lambda user:user['name']==self.name,
                    user.activeUser))[0]
        print(currentuser)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<len(user.activeUser):
            person=user.activeUser[self.index]
            self.index+=1
            return person
        raise StopIteration

me=user('poyan',30)
you=user('farnaz',27)
user3=user('ali',32)
user4=user('mohammad',31)
#print(user.activeUser)
#me.logout()
for person in me:
    print(person)