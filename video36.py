def my_decorator(func):
    def say_bye(*name):
        func(*name)
        print(f'bye {name[0]}')
    return say_bye

@my_decorator
def say_hello(name):
    print(f'hello {name}')

@my_decorator
def say_my_name(name,family):
    print(f'{name} {family}')
#say_hello()
#say_hello=my_decorator(say_hello)
say_hello('poyan')
say_my_name('poyan','rajian')