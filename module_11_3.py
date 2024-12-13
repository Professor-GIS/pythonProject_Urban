# Домашнее задание по теме "Интроспекция"
import inspect
from pprint import pprint


def introspection_info(obj):
	result = {}
	# отделяем лишний текст(<clacss"">)и записываем значение в словарь
	result['type'] = str(type(obj)).split(' ')[1][1:-2]
	# генерируем список атрибутов, исключая служебные и вызываемые(методы); записываем в словарь
	result['atributes'] = [atr for atr in dir(obj) if not atr.startswith('_') and not callable(getattr(obj, atr))]
	# генерируем список методов, которые являются вызываемыми, исключая служебные; записываем в словарь
	result['methods'] = [atr for atr in dir(obj) if not atr.startswith('_') and callable(getattr(obj, atr))]
	# Записываем имя активного модуля в словарь
	result['module'] = __name__
	
	return result


class SomeClass:
	def __init__(self):
		self.attribute_1 = 27
	
	def some_class_method(self, value):
		self.attribute_1 = value
		print(self.attribute_1)


number_info = introspection_info(42)
pprint(number_info)
print()
My_Obj = SomeClass()
number_info = introspection_info(My_Obj)

pprint(number_info)
