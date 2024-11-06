from math import sqrt, pi


class Figure:
	sides_count = 0

	def __init__(self, __color:list, __sides:list, filled = True):
		self.__color = __color
		self.__sides = __sides
		self.filled = filled

	def get_sides(self):
		return self.__sides

	def set_sides(self, *new_sides):
		if len(new_sides) == 1:
			self.__sides = new_sides
			# for i in range(self.sides_count):
			# 	self.__sides += new_sides
		elif len(new_sides) == self.sides_count:
			for i in range(len(new_sides)):
				self.__sides[i] = list(new_sides)[i]
		else:
			print("Неверное количество сторон")


class Circle(Figure):
	sides_count = 1

	def __init__(self, color, *__sides, filled=True, __radius=0):
		if len(__sides) == self.sides_count:
			self.__sides = __sides
		else:
			self.__sides = [1]
		self.__radius = self.__sides[0] / (2 * pi)
		super().__init__(list(color), self.__sides)



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)

# Проверка на изменение сторон:
circle1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(circle1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())



