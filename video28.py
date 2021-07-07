class person:
    def __init__(self,name,family,age,money):
        self.name=name
        self.family=family
        self.age=age
        self.money=money
    def __repr__(self):
        return f'{self.name} {self.family}'
    def __len__(self):
        return self.age
    def __add__(self, other):
        return self.money+other.money
    def __mul__(self, other):
        return self.money * other.money
    def __truediv__(self, other):
        return self.money / other.money
    def __sub__(self, other):
        return self.money - other.money
person1=person('pouyan','rajian',29,3200)
person2=person('ali','ghafori',30,1700)
print(person1)
print(len(person1))
print(person1+person2)
print(person1*person2)
print(person1/person2)
print(person1-person2)



# numbers=[1,2,3,4,5]
# print(len(numbers))