def test_function():
	def inner_function():
		print("Я в области видимости функции test_function")
	inner_function()


test_function()
inner_function() 	#inner_function находится в локальной области имён внутри test_function и не определена на общем
					#уровне global и её вызов с уровня global приведёт к ошибке.
