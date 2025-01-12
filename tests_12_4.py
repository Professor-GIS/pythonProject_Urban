# Домашнее задание по теме "Логирование"


import logging
from rt_with_exceptions import *
import unittest


class RunnerTest(unittest.TestCase):
	
	def test_walk(self):
		try:
			girl = Runner('Jane', -1)
			logging.info(f'"test_walk" выполнен успешно')
			for i in range(10):
				girl.walk()
			self.assertEqual(girl.distance, 50)
		except ValueError:
			logging.warning(f"Неверная скорость для Runner")
		except TypeError:
			logging.warning("Неверный тип данных для имени объекта Runner")
	
	def test_run(self):
		try:
			boy = Runner(2, 10)
			logging.info(f'"test_run" выполнен успешно')
			for i in range(10):
				boy.run()
			self.assertEqual(boy.distance, 100)
		except TypeError:
			logging.warning("Неверный тип данных для имени объекта Runner")
		except ValueError:
			logging.warning(f"Неверная скорость для Runner")
	
	# def test_challenge(self):
	# 	girl = Runner('Ann')
	# 	boy = Runner('Jack')
	# 	for i in range(10):
	# 		girl.walk()
	# 		boy.run()
	# 	self.assertNotEqual(girl.distance, boy.distance)


if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
						format='%(asctime)s | %(levelname)s | %(message)s')
