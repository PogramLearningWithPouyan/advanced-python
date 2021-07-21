# iterable
# iterator
numbers=[1,2,3,4,5,6,7,8,9]
# for num in numbers:
#     print(num)
def myfor(iterable,func):
    iterator=iter(iterable)
    while True:
        try:
            x=next(iterator)
        except StopIteration:
            break
        else:
            func(x)
def powertwo(num):
    print(num**2)

myfor(numbers,powertwo)
# iternumbers=iter(numbers)
# print(next(iternumbers))
# print(next(iternumbers))
# print(next(iternumbers))
# print(next(iternumbers))
# print(next(iternumbers))
# print(next(iternumbers))
