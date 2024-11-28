# Домашнее задание по теме "Потоки на классах"
import threading
from time import sleep


class Knight(threading.Thread):
	def __init__(self, name: str, power: int):
		threading.Thread.__init__(self)
		self.name = name
		self.power = power
	
	def run(self):
		print(f'{self.name}, на нас напали!')
		enemies = 100
		days = 0
		while enemies:
			sleep(1)
			days += 1
			enemies -= self.power
			print(f"{self.name} сражается {days}..., осталось {enemies} воинов.")
		print(f"{self.name} одержал победу спустя {days} дней(дня)!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
# Вывод строки об окончании сражения
while first_knight.is_alive() or second_knight.is_alive():
	sleep(0.1)
print('Все битвы закончились!')
