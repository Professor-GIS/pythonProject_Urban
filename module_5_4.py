# Домашняя работа по уроку "Различие атрибутов класса и экземпляра"

class House:
	houses_history = []

	def __new__(cls, *args, **kwargs):
		instance = super().__new__(cls)
		# В этом месте можно настроить свой экземпляр...
		cls.houses_history.append(args[0])
		return instance

	def __init__(self, *args, **kwargs):
		self.name = args[0]
		self.number_of_floors = args[1]
		self.new_floor = None

	def __del__(self):
		print(f"{self.name} снесён, но он останется в истории")

	def __len__(self):
		return self.number_of_floors

	def __str__(self):
		return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

	def go_to(self, new_floor):
		self.new_floor = int(new_floor)
		if self.number_of_floors < self.new_floor or self.new_floor < 1:
			print("Такого этажа не существует")
		else:
			for i in range(1, self.new_floor + 1):
				print(i)

	def __eq__(self, other):
		return self.number_of_floors == other.number_of_floors

	def __lt__(self, other):
		return self.number_of_floors < other.number_of_floors

	def __le__(self, other):
		return self.number_of_floors <= other.number_of_floors

	def __gt__(self, other):
		return self.number_of_floors > other.number_of_floors

	def __ge__(self, other):
		return self.number_of_floors >= other.number_of_floors

	def __ne__(self, other):
		return self.number_of_floors != other.number_of_floors

	def __add__(self, value):
		self.number_of_floors = self.number_of_floors + value
		return self

	def __iadd__(self, value):
		self.number_of_floors = self.number_of_floors + value
		return self

	def __radd__(self, value):
		self.number_of_floors = self.number_of_floors + value
		return self


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

