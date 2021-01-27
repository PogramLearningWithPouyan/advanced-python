# print(test)
# None=1
# raise SyntaxError ()

def fullname(firstname,lastname):
    if type(firstname) is not str or type(lastname) is not str:
        raise TypeError('please enter str')
    return f'your name is {firstname} {lastname}'

print(fullname(0,'rajian'))