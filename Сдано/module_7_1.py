# Домашнее задание по теме "Режимы открытия файлов"
from pprint import pprint


class Product:
	def __init__(self, name: str, weight: float, category: str):  # Создаём новый экземпляр
		self.name = name  # Задаём аргумент "Название"
		self.weight = weight  # Задаём аргумент "Вес"
		self.category = category  # Задаём аргумент "Категория"

	def __str__(self):  # Переопределяем строку выводимую при вызове экземпляра
		return f'{self.name}, {self.weight}, {self.category}'


class Shop:
	def __init__(self):
		self.__file_name = 'products.txt'  # Инкапсулируем имя файла-базы товаров магазина

	def get_products(self):  # Оформляем вывод содержимого файла-базы товаров магазина
		file = open(self.__file_name, 'r')
		info = file.read()  # Передаём содержимое в переменную, для сохранения после закрытия
		file.close()
		return info

	def add(self, *products: Product):  # Оформляем процесс добавления товаров в файл-базу

		for product in products:  # Перебираем все переданные продукты
			file = open(self.__file_name, 'a')
			if product.name in self.get_products():  # Проверяем нет ли такого продукта в базе
				print(f'Продукт {product.name} уже есть в магазине')  # Ругаемся, если продукт уже есть в базе
			else:

				file.write(f'{product}\n')  # Добавляем в файл базу, если не нашли там такого имени
			file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
