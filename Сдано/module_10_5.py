# Домашнее задание по теме "Многопроцессное программирование"
import time
from multiprocessing import Pool


def read_info(name):
	all_data = []
	with open(name, encoding='utf-8') as file:
		for line in file:
			s = line.rstrip('\n')  # Отделяем символ конца строки для последующей проверки
			if not s == "":  # Проверяем пустая ли строка
				all_data.append(s)
			else:
				break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# start_l = time.time()
# for number in range(1, 5):
# 	read_info(f'./file {number}.txt')
# stop_l = time.time()
# print(stop_l - start_l)

# Многопроцессный вызов
start_m = time.time()
if __name__ == '__main__':
	with Pool(5) as pool:
		pool.map(read_info, filenames)

stop_m = time.time()
print(stop_m - start_m)
