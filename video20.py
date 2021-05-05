class user:
    usercount=0
    allowuser=['pouyan','mohammad','farnaz','mahyar']
    creatuser=[]
    def __init__(self,name,family):
        if name not in user.allowuser:
            raise ValueError(f'{name} is not allow to creat')
        self.username=name
        self.userfamily=family
        user.usercount+=1
        user.creatuser.append(name)
    def deleteuser(self):
        print(f'{self.username} is deleted')
        user.usercount-=1
        user.creatuser.remove(self.username)


pouyan=user('pouyan','rajian')
mohammad=user('mohammad','nori')
# print(id(pouyan.allowuser))
# print(id(mohammad.allowuser))
# print(id(user.allowuser))

pouyan.allowuser.append('ali')
print(user.allowuser)
print(pouyan.allowuser)
# print(user.usercount)
# print(user.creatuser)
# pouyan=user('pouyan','rajian')
# print(user.usercount)
# print(user.creatuser)
# ali=user('mohammad','nori')
# print(user.usercount)
# print(user.creatuser)
# pouyan.deleteuser()
# print(user.usercount)
# print(user.creatuser)
