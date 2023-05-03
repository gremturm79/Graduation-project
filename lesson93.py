
import python_weather
import asyncio
import os

d = ['температура', 'скорость ветра', 'направление ветра', 'давление', 'влажность', 'описание']
lst = []


async def getweather():

    async with python_weather.Client(format=python_weather.METRIC) as client:
        weather = await client.get('Berlin')
        lst = [weather.current.temperature, weather.current.wind_speed, weather.current.wind_direction,
               weather.current.pressure, weather.current.humidity, weather.current.type]
        meteo = []
        for i in range(len(d)):
            meteo.append(str(d[i]))
            meteo.append(str(lst[i]))
        print(' '.join(meteo))


if __name__ == "__main__":
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())
