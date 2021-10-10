# test_text=open('./text.txt')
# print(test_text.read())
# test_text.close()
# print(test_text.read())

# test_text.seek(1)
# print(test_text.read())
# print(test_text.readline())
# print(test_text.readline())
# print(test_text.readline())
# test_text.seek(1)
# print(test_text.readline())
# test_list=test_text.readlines()
# print(test_list)

with open('./text.txt',mode='a') as test_file:
    test_file.write('this chanel name is program learning with pouyan\n')

with open('./text.txt', mode='a') as test_file:
    test_file.write('my name is pouyan\n')


with open('./text.txt',mode='a') as test_file:
    test_file.write('hello guys\n')
