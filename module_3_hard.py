def calculate_structure_sum(data, summ_=None):
	if isinstance(data, int|float):
		summ_ += data
	elif isinstance(data, str):
		summ_ += len(data)
	elif isinstance(data, list):
		if len(data) ==1:
			
		if isinstance(i, list):
			for j in i:

	return summ_




data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

print(len('a'))