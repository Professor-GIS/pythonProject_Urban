# Домашнее задание по теме "Создание исключений"


class Car:  # Создаём экземпляр класса
	def __init__(self, model: str, __vin: int, __numbers: str):
		self.model = model
		if self.__is_valid_vin(__vin):  # Проверяем соответствует ли vin требованиям через специальный метод
			self.__vin = __vin  # Если соответствует - задаём инкапсулированный атрибут __vin
		if self.__is_valid_numbers(__numbers):  # Проверяем соответствует ли номер требованиям через специальный метод
			self.__numbers = __numbers  # Если соответствует - задаём инкапсулированный атрибут __numbers

	def __is_valid_vin(self, vin_number):  # Метод проверяющий vin на соответствие требованиям
		if not isinstance(vin_number, int):  # Если тип данных НЕ int - выдаём ошибку с сообщением
			raise IncorrectVinNumber('Некорректный тип vin номер')
		else:
			if 1000000 > vin_number < 9999999:  # Проверяем диапазон vin, иначе выдаём ошибку с сообщением
				raise IncorrectVinNumber('Неверный диапазон для vin номера')
		return True  # Если проверки прошли без ошибок - возвращаем True

	def __is_valid_numbers(self, car_numbers):
		if not isinstance(car_numbers, str):  # Если тип данных НЕ str - выдаём ошибку с сообщением
			raise IncorrectCarNumbers('Некорректный тип данных для номеров')
		else:
			if not len(car_numbers) == 6:  # Если длинна номера НЕ 6 знаков - выдаём ошибку с сообщением
				raise IncorrectCarNumbers('Неверная длина номера')
		return True  # Если проверки прошли без ошибок - возвращаем True


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
