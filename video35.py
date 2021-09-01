# def sumTo(number,func):
#     total=0
#     for num in range(1,number+1):
#         total+=func(num)
#     return total
# def squere(x):
#     return x*x
#
# print(sumTo(5,squere))
#1+2+3+4+5=15
#1+4+9+16+25=55

from random import choice
# def greet(person):
#     def get_mood():
#         msg=choice(('hello ','hi ','good morning ','bye '))
#         return msg
#     result=get_mood()+person
#     return result

def greet(person):
    def get_mood():
        msg=choice(('hello ','hi ','good morning ','bye '))+person

        return msg

    return get_mood
result=greet('ali')
print(result())