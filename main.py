class Figure:
	sides_count = 0

	def __init__(self, __color: list, __sides: list, filled=True):
		self.__color = list(__color)
		self.__sides = list(__sides) #тут нужна проверка на количество и правильность сторон

class Circle(Figure):
	sides_count = 1

	def __init__(self, color, *__sides, filled=True, __radius=0):
		super().__init__(color, __sides)
		self.__radius = __sides[0] / (2 * pi)