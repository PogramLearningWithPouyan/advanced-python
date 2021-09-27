from time import time
# strat=time()
# sum(num for num in range(5000000))
# end=time()
# print(end-strat)

def speed_test (func):
    def wrapper(*args,**kwargs):
        strat=time()
        result=func(*args,**kwargs)
        end=time()
        print(end-strat)
        return result
    return wrapper

@speed_test
def sum_num_list():
    return sum(num for num in range(500000000))

@speed_test
def sum_num_gen():
    return sum([num for num in range(500000000)])
sum_num_list()
sum_num_gen()