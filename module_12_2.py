# Домашнее задание по теме "Методы Юнит-тестирования"

from runner_turnament import *
import unittest


class TournamentTest(unittest.TestCase):
	is_frozen = True
	
	@classmethod
	def setUpClass(cls):
		cls.all_results = {}
	
	def setUp(self):
		self.r_1 = Runner('Усейн', 10)
		self.r_2 = Runner('Андрей', 9)
		self.r_3 = Runner('Ник', 3)
	
	@classmethod
	def tearDownClass(cls):
		for i in cls.all_results:
			print(cls.all_results[i])
	
	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_1(self):
		t_1 = Tournament(90, (self.r_1, self.r_3))
		self.all_results[1] = t_1.start()
		self.assertTrue((self.all_results[1])[2] == 'Ник')
	
	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_2(self):
		t_2 = Tournament(90, (self.r_2, self.r_3))
		self.all_results[2] = t_2.start()
		self.assertTrue((self.all_results[2])[2] == 'Ник')
	
	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_3(self):
		t_3 = Tournament(90, (self.r_1, self.r_2, self.r_3))
		self.all_results[3] = t_3.start()
		self.assertTrue((self.all_results[3])[3] == 'Ник')
