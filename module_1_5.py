immutable_var = (1, 's', [1, 2])
print(immutable_var)
# Изменить первые два элемента в кортеже нельзя, т.к. они сами по себе "не изменяемые", а вот последний элемент "список" можно изменить
#immutable_var[0] = 0
#immutable_var[2][0] = 2

mutable_list = [1, 2, 'a', 'b']
mutable_list.append('Modified')
print(mutable_list)
