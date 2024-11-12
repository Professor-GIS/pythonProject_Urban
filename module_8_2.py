# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции"


def personal_sum(numbers):
	result = 0
	incorrect_data = 0
	for n in numbers:
		try:
			result += n
		except TypeError as exc:
			incorrect_data += 1
			print(f'Некорректный тип данных для подсчёта суммы - {n}')
	return result, incorrect_data


def calculate_average(numbers):
	try:
		r, i = personal_sum(numbers)
		average = r / (len(numbers) - i)
	except ZeroDivisionError as exc:
		return 0
	except TypeError as exc:
		print(f'В numbers записан некорректный тип данных')
		return None
	return average


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
