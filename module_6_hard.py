# Дополнительное практическое задание по модулю*
from math import sqrt, pi


class Figure:
	sides_count = 0

	def __init__(self, __color: list, __sides: list, filled=True):
		self.__color = list(__color)
		if len(__sides) != self.sides_count:
			if len(__sides) == 1:
				self.__sides = list(__sides) * self.sides_count
			else:
				self.__sides = [1] * self.sides_count
		elif len(__sides) == 1:
			self.__sides = list(__sides)
		elif len(__sides) == 3:
			lst = list(__sides)
			if lst[0] > (lst[1] + lst[2]) or lst[1] > (lst[2] + lst[0]) or lst[2] > (lst[1] + lst[0]):
				print("Длинна одной стороны не может быть больше суммы двух других.")
			else:
				self.__sides = list(__sides)
		elif len(__sides) == 12:
			if len(set(__sides)) != 1:
				print("Все стороны куба должны быть равны.")
			else:
				self.__sides = list(__sides)
		self.filled = filled

	def get_color(self):
		return self.__color

	def __is_valid_color(self, r, g, b):
		return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

	def set_color(self, r, g, b):
		if self.__is_valid_color(r, g, b):
			self.__color[0] = r
			self.__color[1] = g
			self.__color[2] = b

	def __is_valid_sides(self, *sides):
		flag = 1
		sides_list = list(sides)
		if len(sides_list) == self.sides_count:
			for i in sides_list:
				if i != int(i) and i <= 0:
					flag = 0
		if flag == 1:
			return True
		else:
			return False

	def get_sides(self):
		return self.__sides

	def __len__(self):
		return sum(self.__sides)

	def set_sides(self, *new_sides):
		if len(new_sides) == self.sides_count:
			if len(new_sides) == self.sides_count:
				for i in range(len(new_sides)):
					self.__sides[i] = list(new_sides)[i]
	# else:
	# 	print("Неверное количество сторон для замены.")


class Circle(Figure):
	sides_count = 1

	def __init__(self, color, *__sides, filled=True, __radius=0):
		super().__init__(color, __sides)
		self.__radius = __sides[0] / (2 * pi)

	def get_square(self):
		return pi * (self.__radius ** 2)


class Triangle(Figure):
	sides_count = 3

	def __init__(self, color, *__sides, filled=True):
		super().__init__(color, __sides)

	def get_square(self):
		a = self.__sides[0]
		b = self.__sides[1]
		c = self.__sides[2]
		p = (a + b + c) / 2
		s = sqrt(p * (p - a) * (p - b) * (p - c))
		return s


class Cube(Figure):
	sides_count = 12

	def __init__(self, color, *__sides, filled=True):
		super().__init__(color, __sides)
		x = self._Figure__sides
		self.__sides = x

	def get_volume(self):
		return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

