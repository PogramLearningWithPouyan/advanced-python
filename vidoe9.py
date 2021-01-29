try:
    print(test)
except:
    print('an eroor occured')
def personkey(diction,key):
    try:
        print(person[key])
    except ValueError:
        print(None)
    except KeyError:
        print('key error')
    else:
        print('this is else')
    finally:
        print('this is finally')

person={'name':'pouyan','family':'rajian'}

personkey(person,'name')