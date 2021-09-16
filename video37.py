from functools import wraps
# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args):
#         print(f'function name is {func.__name__}')
#         func(*args)
#     return wrapper
#
# @my_decorator
# def say_hello(name,family):
#     print(f'hello {name} {family}')
#
# #say_hello('poyan','rajian')
# print(say_hello.__name__)
# help(say_hello)
# def show_decorator(is_show):
#     def run_decorator(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             if is_show:
#                 func()
#             else:
#                 print("you don't have permission")
#         return wrapper
#     return run_decorator
#
# @show_decorator(False)
# def admin():
#     print('this is admin')
#
# admin()

def check_string_lenght(charecterCount):
    def inner_decorator(func):
        @wraps(func)
        def wrapper(name):
            if len(name)<charecterCount:
                func(name)
            else:
                #raise ValueError('an error occurd')
                print('lenght of name in high')
        return wrapper
    return inner_decorator

@check_string_lenght(10)
def show_name(name):
    print(name)

show_name('poyan rajian')