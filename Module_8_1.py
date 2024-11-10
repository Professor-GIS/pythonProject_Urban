# Домашнее задание по теме "Try и Except"

def add_everything_up(a, b):
	try:
		x = round(a + b, 3)
	except TypeError:
		return f'{str(a)}{str(b)}'
	else:
		return x


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
