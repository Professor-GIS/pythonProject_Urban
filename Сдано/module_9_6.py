# Домашнее задание по теме "Генераторы"


def all_variants(text):
	for num in range(len(text)):
		for j in range(len(text) - num):
			yield text[j:j + num + 1]


a = all_variants("abc")
for i in a:
	print(i)
