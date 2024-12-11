# Домашнее задание по теме "Обзор сторонних библиотек Python"
import requests
import pprint

BASE_URL = "https://api.open-meteo.com/v1/forecast"
# Запрос погоды в Волгограде
params = {
	"latitude": 48.7089,  # широта Волгограда
	"longitude": 44.5144,  # долгота Волгограда
	"daily": "temperature_2m_min,temperature_2m_max,precipitation_sum,sunrise,sunset",
	# минимальная и максимальная температура, сумма осадков, время восхода и захода солнца
	"timezone": "Europe/Moscow"  # временная зона Москвы
}
response = requests.get(BASE_URL, params=params)
if response.status_code == 200:
	data = response.json()
	# Поскольку индекс 0 представляет собой данные на текущий день, индекс 1 будет представлять данные на завтра
	tomorrow_temp_min = data['daily']['temperature_2m_min'][1]
	tomorrow_temp_max = data['daily']['temperature_2m_max'][1]
	tomorrow_precipitation = data['daily']['precipitation_sum'][1]
	tomorrow_sunrise = data['daily']['sunrise'][1]
	tomorrow_sunset = data['daily']['sunset'][1]
	
	print(f"Прогноз погоды в Москве на завтра:")
	print(f"Минимальная температура: {tomorrow_temp_min}°C")
	print(f"Максимальная температура: {tomorrow_temp_max}°C")
	print(f"Ожидаемое количество осадков: {tomorrow_precipitation} мм")
	print(f"Время восхода солнца: {tomorrow_sunrise}")
	print(f"Время захода солнца: {tomorrow_sunset}")
else:
	print(f"Ошибка {response.status_code}: {response.text}")



from PIL import Image

#Загрузим фото из интернета и сохраним его для дальнейшей обработки
with open('photo.png', 'wb') as target:
	photo = requests.get('https://sun9-19.userapi.com/impf/c627518/v627518696/314b/5jV_G2QVm0g.jpg?size=807x538&quality=96&sign=03c57ab15f301b86941f3db93dc6b848&type=album')
	target.write(photo.content)
# Загрузим фото в память для дальнейшей работы
# with Image.open('photo.png') as img:
with Image.open('photo.png') as img:
	img.load()
# Сделаем чёрно-белую версию
gray_img = img.convert("L")
#Создадим пустой шаблон под 2хфото
new_image = Image.new('RGB',(2*img.size[0], img.size[1]), (250,250,250))

#вставляем наши изображения по горизонтали
new_image.paste(img,(0,0))
new_image.paste(gray_img,(img.size[0],0))

#смотрим, что получилось
new_image.show()


