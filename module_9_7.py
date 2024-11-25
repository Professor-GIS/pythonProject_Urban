# Домашнее задание по теме "Декораторы"

def is_prime(func):
	def wrapper():
		res = func()  # Сохраняем результат работы исходной функции в переменную для оценки
		
		d = 2  # Проверяем, является ли полученная сумма простым числом и выводим соответствующее сообщение
		while d * d <= res and res % d != 0:
			d += 1
		if d * d > res:
			print("Простое")
		else:
			print("Составное")
		return func
	
	return wrapper()


@is_prime  # Используем декоратор
def sum_three(*args):
	summ = sum(args)
	return summ


result = sum_three(2, 3, 6)
print(result)
