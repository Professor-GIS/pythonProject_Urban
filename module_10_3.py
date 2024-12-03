# Домашнее задание по теме "Блокировки и обработка ошибок"
import threading
from random import randint
from time import sleep


class Bank:
	def __init__(self):
		self.balance = 0
		self.lock = threading.Lock()
	
	def deposit(self):
		for i in range(100):
			incr = randint(50, 500)
			self.balance += incr
			if self.balance >= 500 and self.lock.locked():#Проверяем размер баланса и не включена ли блокировка потока
				self.lock.release()
				sleep(0.01)  # Добавляем задержку после снятия замка, чтобы не наслаивались принты из разных потоков
			print(f'Пополнение: {incr}. Баланс: {self.balance}')
			sleep(0.001)
	
	def take(self):
		for i in range(100):
			decr = randint(50, 500)
			print(f'Запрос на {decr}.')
			if decr <= self.balance:
				self.balance -= decr
				print(f'Снятие: {decr}. Баланс: {self.balance}')
			else:
				print(f'Запрос отклонён, недостаточно средств')
				self.lock.acquire()#Включаем блокировку и дожидаемся наполнения баланса 500+


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
