from weather import Weather
from translate import Translator


def forecast(city):
    lst = []
    weather = Weather(temperature_unit='Celsius')  # установка параметров измерения температуры
    current_weather = weather.fetch_weather(city=city, only_temp=True)  # принимает параметр City, возвращает
    # словарь
    # город температура влажность облачность

    translator = Translator(from_lang='en', to_lang='ru')  # установка языка в который необходимо перевести
    current_weather['Pressure: '] *= 0.76
    print(current_weather)
    for i in current_weather:  # перевод атмосферного давления в мм.рт. столба и добавления ключей и значений словаря в
        # список
        print(i)
        pairs = list(current_weather.items())
        for i in range(len(pairs)):
            if i == 3:
                continue
        pairs[i] = translator.translate(pairs[i])
        lst = ' '.join(lst)
    return lst


forecast('Berlin')
