class user:
    username='pouyan'
    userfamily='rajian'
    userage=29

    def showfullname(self):
        return f'{self.username} {self.userfamily}'

# print(type(56))
# numlist=list()
# print(type(numlist))
pouyan=user()
# print(type(pouyan))
# print(__name__)
print(pouyan.username)
print(pouyan.showfullname())