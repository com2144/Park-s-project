"""
City Environment can write down the city name, date, and time.
The corresponding value shows the position of the sun, the illuminance of the sun, and the weather.

City Environment will help vfx artist position light.

City Environment is available in python 3.9.

Here's how to use it.
#####################################
import cityEnvironment

t = cityEnvironment.CityEnvironment()
t.city_name = 'Tokyo'
t.date = '2023/01/26'
t.time = '16:19:00'
print(t.sun_position())
print(t.weather_condition())
print(t.sun_light_amount())
####################################
#'t' is an example variable.

CAUTION!! Avoid repeated statements when printing weather_condition and sun_light_amount.
If you output continuously, you may lose connection with the weather api server.
"""
