n = int(input("Ведите первое число (3-20): "))
result = ""
for i in range(1, (n // 2) + 1):
	for j in range(i + 1, n):
		if n % (i + j) == 0:
			result += f'{i}{j}'
print("Второе число:", int(result))
