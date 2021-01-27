# num1=[1,2,3,4]
# num2=[5,6,7,8]
# rusult=zip(num2,num1)
# print(dict(rusult))
# print(list(rusult))
# mylist=[(1,2),(3,4),(5,6)]
# res=zip(*mylist)
# print(list(res))
students=['pouyan','ali','mohammad']
midterm1=[80,89,75]
midterm2=[90,88,60]
midterm3=[83,70,76]
#{'pouyan':90,}
# bestscore=[max(num) for num in zip(midterm3,midterm1,midterm2)]
# studentscore={personscore[0]:max(personscore[1],personscore[2]
#                                  ,personscore[3]) for personscore
#               in zip(students,midterm3,midterm1,midterm2)}
studentscore2=zip(students,map(lambda perscore: max(perscore),
                               zip(midterm3,midterm2,midterm1)))
print(dict(studentscore2))