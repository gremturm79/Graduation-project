from appyweather import Weather

# using a city name
weather = Weather(api_key='8eb0ec61db7b93e0eb2c74716c8e6c8f', city='Kaliningrad', units='metric')

# using latitude/longitude coordinates + units (optional)
# weather1 = Weather(api_key='yourapikeyhere', lat=37.98, lon=23.72, units='metric')

# get full 3-hour weather data for the next 24 hours
w = weather.next_24_hours()
print(type(w))
for i in range(len(w)):
    for j in w[i]:
        if i == 1:
            if j == 'main_1' or j == 'weather' or j == 'wind':
                print(w[i][j])
                #for k in w[i][j]:
                    #print(k, w[i][j][k])
            else:
                continue



# get basic 3-hour weather data for the next 24 hours
# weather1.next_24_hours_basic()
