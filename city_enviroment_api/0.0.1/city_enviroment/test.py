import cityEnvironment

t = cityEnvironment.CityEnvironment()
t.city_name = 'Tokyo'
t.date = '2023/01/26'
t.time = '16:19:00'
print(t.sun_position())
print(t.weather_condition())
print(t.sun_light_amount())