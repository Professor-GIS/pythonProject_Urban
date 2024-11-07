my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict.get('Vasya'))
print(my_dict.get('Oleg',''))
my_dict.update({'Kamila': 1981, 'Artem': 1915})
print(my_dict.pop('Egor'))
print(my_dict)


my_set = {1, 2, 3, 2, 1, 'Яблоко', 42.314}
print(my_set)
my_set.add(4)
my_set.add( 'Window')
my_set.discard(2)
print(my_set)

