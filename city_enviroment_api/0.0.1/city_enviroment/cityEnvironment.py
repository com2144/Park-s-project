"""
Used 're' for character substitution.
Used 'ephem' for the position of the sun.
Used 'Nominatim' to get the location information of the map.
(The city information of 'ephem' is limited.)
Used 'requests' to get the web's weather history.
"""
import re
import ephem
from geopy.geocoders import Nominatim
import requests


class CityEnvironment:

    def __init__(self):
        """
        The initial blank city_name, _date, and _time are the values that the user wants.

        The _latitude and _longitude values change depending on
        what value city_name is put in the location.

        CAUTION!! Avoid repeated statements when printing weather_condition and sun_light_amount.
        If you output continuously, you may lose connection with the weather api server.
        """
        self._city_name = ""
        self._date = ""
        self._time = ""
        self._latitude = None
        self._longitude = None
        self._key = '6XVD6S2PSXKEM6PCH5C2YAZLP'
        self._response = None
        self._api_data = None

    @property
    def city_name(self) -> str:
        """

        Returns: Defines an empty city name.

        """
        return self._city_name

    @city_name.setter
    def city_name(self, value) -> str:
        """

        Args:
            value: capitalize the city name that the user wants.

        Returns: city name

        """
        if not isinstance(value, str):
            raise ValueError('Write down the string.')
        if value[0].islower():
            raise ValueError('The first letter of the city name must be capitalized.')
        if not value.isalpha():
            raise ValueError('Enter a city name.')
        self._city_name = value

    """
    Call the city name with "city_name".
    """

    @property
    def date(self) -> str:
        """

        Returns: Defines an empty date.

        """
        return self._date

    @date.setter
    def date(self, value) -> str:
        """

        Args:
            value: str -> Write between the ":" positions in
            the year, mouth, and day that the user wants.

        Returns: year, mouth, day

        """
        date_match = re.match(r'([0-9]+)/([0-9]+)/([0-9]+)', value)
        if date_match is None:
            raise ValueError('Put a date between the "/" positions. Put data format : 22/01/01')
        self._date = value

        """
        "date" calls the date.
        """

    @property
    def time(self) -> str:
        """

        Returns: Defines an empty time.

        """
        return self._time

    @time.setter
    def time(self, value) -> str:
        """

        Args:
            value: str -> Write between the ":" positions in
            the hour, minute, and seconds that the user wants.

        Returns: hour, minute, seconds

        """
        time_match = re.match(r'([0-9]+):([0-9]+):([0-9]+)', value)
        if time_match is None:
            raise ValueError('Put a time between the ":" positions.')
        self._time = value

        """
        "time" calls the time.
        """

    @property
    def _analyze(self) -> str:
        """

        Returns: Call user_agent="geoapiExercises" with Nominatim.
        The geolocator.geocode returns the location value corresponding to the city name.

        """
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(self.city_name)
        # ephem.city(self._name)
        return location

    @property
    def latitude(self) -> str:
        """

        Returns: the latitude of the called city.

        """
        return self._analyze.latitude
        # return self.analyze.lat

    @property
    def longitude(self) -> str:
        """

        Returns: the longitude of the called city.

        """
        return self._analyze.longitude
        # return self.analyze.lon

    def sun_position(self) -> dict:
        """

        Returns: the position of sun from the observer's point of view.

        """
        """
        1. Create an empty observer.
        2. Enter the initial values of the Earth's axis of rotation and atmospheric pressure with the observer.
        4. Overwrite the latitude and longitude of the city being an observer.
        5. Apply the date and time of the city to the observer.
        6. Calculate the relationship between the city and the year that are observers.
        7. After deriving the location, you can choose whether to receive the actual angle value or
           the longitude and latitude values on the map.
        """
        observer = ephem.Observer()
        observer.pressure = 0
        observer.horizon = '-0:34'
        observer.lat = self.latitude
        observer.lon = self.longitude
        observer.date = self.date + ' ' + self.time
        sun = ephem.Sun()
        sun.compute(observer)
        data = {
            'actual angle': [sun.az.__repr__(), sun.alt.__repr__()],
            'map angle': [sun.az.__str__(), sun.alt.__str__()]
        }
        return data

    @property
    def _weather_api_install(self) -> str:
        """

        Returns: Called in to find out the illumination value of
        the sun and the weather conditions.

        """
        if self.city_name and self.date:
            city_ = self.city_name
            city_[0].lower()
            date_ = re.sub("/", "-", self.date)
            api = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' \
                  f'{city_}/{date_}/{date_}?unitGroup=metric&key={self._key}&contentType=json'
            self._response = requests.get(api)
            return self._response
        else:
            raise ValueError('You have both a city name and a date.')

    @property
    def _weather_api_response(self) -> str:
        """

        Returns: It informs the server response and response code of weather api.

        """
        self._weather_api_install()
        if self._response is None:
            raise ValueError('The server is unresponsive.')
        if self._response.status_code != "200":
            raise ValueError(f'Status Error : {self._response.status_code}')
        self._api_data = self._response.json()

    def weather_condition(self) -> str:
        """

        Returns: After connecting with weather api,
        it tells you about the weather conditions.

        """
        self._weather_api_response()
        for weather_info in self._api_data:
            weather = weather_info['icon']
            return weather

    def sun_light_amount(self) -> str:
        """

        Returns: After connecting with weather api,
        it tells you about the illumination of the sun.

        """
        self._weather_api_response()
        for weather_info in self._api_data:
            solar = weather_info['solarradiation']
            return solar
