# Домашнее задание по теме "Систематизация и пропуск тестов".


import unittest
import module_12_1
import module_12_2

my_suite_test = unittest.TestSuite()
my_suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
my_suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(my_suite_test)
