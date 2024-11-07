# Домашнее задание по теме "Оператор "with".

class WordsFinder:
	def __init__(self, *files):
		self.file_names = list(files)  # Задаём список имён файла

	def get_all_words(self):
		all_words = {}
		sym = [',', '.', '=', '!', '?', ';', ':', ' - ']  # Создаём список со знаками препинания которые надо удалить
		for name in self.file_names:  # Перебираем имина файлов из переданного списка
			with open(name, encoding='utf-8') as file:  # Открываем каждый файл из списка
				words_in_lines = []  # Обнуляем список если он был заполнен предыдущим файлом
				for line in file:  # Перебираем построчно все строки в файле
					new_line = line.lower()  # Исключаем влияние заглавных букв
					for j in sym:  # Перебираем символы для удаления знаков препинания
						new_line = new_line.replace(j, '')
					words_in_lines += (new_line.split())  # Добавляем в список слова разделённые пробелами
				all_words[name] = words_in_lines  # Заполняем словарь для вывода
		return all_words

	def find(self, word):
		found = {}
		word = word.lower()  # Исключаем влияние заглавных букв
		for name, words in self.get_all_words().items():  # Перебираем ключи и значения в словаре из метода выше
			if word in words:
				found[name] = words.index(word) + 1  # Если слово есть в списке слов - создаём словарь с его номером
		return found

	def count(self, word):
		counted = {}
		word = word.lower()  # Исключаем влияние заглавных букв
		for name, words in self.get_all_words().items():  # Перебираем ключи и значения в словаре из первого метода
			if word in words:
				counted[name] = words.count(word)  # Если слово есть в списке слов - создаём словарь с их количеством
		return counted


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
					  'Rudyard Kipling - If.txt',
					  'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
