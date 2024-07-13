students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(list(students))
sorted_students=sorted(students)
print('List students:',sorted_students)
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
total0=sum(grades[0])/len(grades[0])
total1=sum(grades[1])/len(grades[1])
total2=sum(grades[2])/len(grades[2])
total3=sum(grades[3])/len(grades[3])
total4=sum(grades[4])/len(grades[4])
list_students={sorted_students[0]:total0,sorted_students[1]:total1,sorted_students[2]:total2,
               sorted_students[3]:total3,sorted_students[4]:total4}
print((list_students))