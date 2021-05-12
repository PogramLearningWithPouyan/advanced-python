class user:
    def __init__(self, name, family, age):
        self.username = name
        self.userfamily = family
        self.userage = age

    def __repr__(self):
        return f'{self.username} {self.userfamily} is {self.userage}'

    def __add__(self, other):
        return self.userage + other.userage

    def __sub__(self, other):
        return self.userage - other.userage


me = user('pouyan', 'rajian', 30)
print(me)
you = user('ali', 'ghafori', 28)
print(you)
print(me + you)
print(me - you)