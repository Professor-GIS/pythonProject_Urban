# Домашнее задание по теме "Простые Юнит-Тесты"

from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
	is_frozen = False
	
	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_walk(self):
		girl = Runner('Jane')
		for i in range(10):
			girl.walk()
		self.assertEqual(girl.distance, 50)
	
	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_run(self):
		boy = Runner('John')
		for i in range(10):
			boy.run()
		self.assertEqual(boy.distance, 100)
	
	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_challenge(self):
		girl = Runner('Ann')
		boy = Runner('Jack')
		for i in range(10):
			girl.walk()
			boy.run()
		self.assertNotEqual(girl.distance, boy.distance)
