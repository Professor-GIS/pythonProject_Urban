grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_list = list(students)
student_list.sort()
my_dict={}
for i in range(len(grades)):
    my_dict[student_list[i]] = sum(grades[i])/len(grades[i])
print(my_dict)
