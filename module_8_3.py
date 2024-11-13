# Домашнее задание по теме "Создание исключений"


class Car:  # Создаём экземпляр класса
	def __init__(self, model: str, __vin: int, __numbers: str):
		self.model = model
		if self.__is_valid_vin(__vin):
			self.__vin = __vin
		if self.__is_valid_numbers(__numbers):
			self.__numbers = __numbers

	def __is_valid_vin(self, vin_number):
		if not isinstance(vin_number, int):
			raise IncorrectVinNumber('Некорректный тип vin номер: vin должен быть целым числом (int)')
		else:
			if 1000000 > vin_number < 9999999:
				raise IncorrectVinNumber('Неверный диапазон для vin номера: vin должен быть в диапазоне 1000000-9999999')
		return True

	def __is_valid_numbers(self, car_numbers):
		if not isinstance(car_numbers, str):
			raise IncorrectCarNumbers('Некорректный тип данных для номеров: номер должен быть строковым значением (str)')
		else:
			if not len(car_numbers) == 6:
				raise IncorrectCarNumbers('Неверная длина номера: номер должен состоять из 6 знаков')
		return True


class IncorrectVinNumber(Exception):
	def __init__(self, message):
		self.message = message


class IncorrectCarNumbers(Exception):
	def __init__(self, message):
		self.message = message


try:
	first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
	print(exc.message)
except IncorrectCarNumbers as exc:
	print(exc.message)
else:
	print(f'{first.model} успешно создан')

try:
	second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
	print(exc.message)
except IncorrectCarNumbers as exc:
	print(exc.message)
else:
	print(f'{second.model} успешно создан')

try:
	third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
	print(exc.message)
except IncorrectCarNumbers as exc:
	print(exc.message)
else:
	print(f'{third.model} успешно создан')
