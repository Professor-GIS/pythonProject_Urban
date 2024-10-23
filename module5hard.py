# Дополнительное практическое задание по модулю: "Классы и объекты."
import time

class User:

	def __init__(self, nickname, password, age: int):
		self.nickname = str(nickname)
		self.password = str(password)
		self.age = int(age)

	def __str__(self):
		return self.nickname


class Video:
	def __init__(self, title, duration, time_now=0, adult_mode=False):
		self.title = title
		self.duration = duration
		self.time_now = time_now
		self.adult_mode = bool(adult_mode)


class UrTube:

	def __init__(self, users=[], videos=[], current_user=None):

		self.users = users
		self.videos = videos
		self.current_user = current_user

	def login(self, nickname, password):
		for i in self.users:
			if nickname in i.nickname:
				if hash(password) == hash(i.password):
					self.current_user = i

	def register(self, nickname, password, age):
		fl = 0
		for i in self.users:
			if i.nickname == nickname:
				fl = 1
				break
		if fl == 1:
			print(f"Пользователь {nickname} уже существует")
		else:
			self.users.append(User(nickname, password, age))
			self.login(nickname, password)

	def log_out(self):
		print(f"Завершаем сеанс пользователя {self.current_user}")
		self.current_user = None

	def add(self, *args):
		for arg in args:
			if len(self.videos)==0:
				self.videos.append(arg)
				continue
			else:
				fl = 0
				for i in self.videos:
					if i.title == arg.title:
						fl = 1
						break
				if fl == 0:
					self.videos.append(arg)

	def get_videos(self, txt):
		found=[]
		for i in self.videos:
			if txt.lower() in i.title.lower():
				found.append(i.title)
		return found

	def watch_video(self, txt):
		for i in self.videos:
			if i.title == txt:
				if self.current_user is None:
					print("Войдите в аккаунт, чтобы смотреть видео")
					break
				elif self.current_user.age < 18 and i.adult_mode:
					print("Вам нет 18 лет, пожалуйста покиньте страницу")
					break
				else:
					while i.time_now < i.duration:
						i.time_now += 1
						print(i.time_now)
						time.sleep(1)
					print("Конец видео")
					i.time_now = 0



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
#ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')