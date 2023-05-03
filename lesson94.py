from OpenweatherPy import WeatherPy
from translate import Translator

translator = Translator(from_lang='en', to_lang='ru')
weather = WeatherPy('8eb0ec61db7b93e0eb2c74716c8e6c8f')
city = weather.query(city='Sochi')
city1 = translator.translate(city.name)
t = city.temperature - 273, 15
t1 = round(t[0], 1)
d = city.pressure / 1.3
d1 = round(d, 1)
w = city.wind
w1 = w['speed']
a = ['город:', city1]
b = ['температура:', t1]
c = ['влажность:', city.humidity]
d = ['давление:', d1]
e = ['cкорость ветра:', w1]
lst = a + b + c + d + e
lst1 = list(map(str, lst))
forecast = ' '.join(lst1)
print(forecast)
