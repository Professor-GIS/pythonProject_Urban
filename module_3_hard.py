def calculate_structure_sum(data):
	if isinstance(data, int):
		return data
	elif isinstance(data, str):
		return len(data)
	elif isinstance(data, list | tuple):
		if len(data) == 0:
			return 0
		if len(data) == 1:
			return calculate_structure_sum(data[0])
		else:
			return calculate_structure_sum(data[0]) + calculate_structure_sum(data[1:])
	elif isinstance(data, set):
		return calculate_structure_sum(list(data))
	elif isinstance(data, dict):
		return calculate_structure_sum(list(data.keys())) + calculate_structure_sum(list(data.values()))


data_structure = [
	[1, 2, 3],
	{'a': 4, 'b': 5},
	(6, {'cube': 7, 'drum': 8}),
	"Hello",
	((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
