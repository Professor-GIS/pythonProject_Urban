# Домашнее задание по теме "Форматирование строк".
# Пример входных данных
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
	result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
	result = 'Победа команды Волшебники Данных!'
else:
	result = 'Ничья!'
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

#	Использование %:
print("В команде Мастера кода участников: %(team1_num)s ! " % {'team1_num': '5'})
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s !" % {'team1_num': '5', 'team2_num': '6'})

#	Использование format():
print("Команда Волшебники данных решила задач: {score_2} !".format(score_2=42))
print("Волшебники данных решили задачи за {team2_time} с !".format(team2_time=2153.31451))

# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')

