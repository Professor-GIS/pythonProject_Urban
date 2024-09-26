#1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
	print(a, b, c)


print_params(0, 25, [1, 2, 3])  # передача в функцию типов данных отличных от "поумолчанию" - работает
print_params(b = 25)
print_params(c = [1,2,3])
print_params(28, 'Python')
print_params()


#2.Распаковка параметров:
values_list = [1, 2.5, 'string']
values_dict = {'a': 0, 'b': [1,2], 'c': False}
print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
