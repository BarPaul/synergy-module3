# Нужные импорты
from requests import get, exceptions
from dataclasses import dataclass
from config import URL, CODES


# Датакласс для хранения погоды
@dataclass
class Weather:
    time: str
    interval: int
    temperature_2m: float
    relative_humidity_2m: int
    apparent_temperature: float
    precipitation: float
    rain: float
    showers: float
    snowfall: float
    weather_code: int
    cloud_cover: int
    pressure_msl: float
    surface_pressure: float
    wind_speed_10m: float
    wind_direction_10m: int
    wind_gusts_10m: float


def get_weather(latitude: float, longitude: float) -> Weather | str:
    'Функция получения погоды по координатам'
    # Конструкция try/except для обработки ошибок во время запроса
    try:
        return Weather(**get(URL.format(latitude, longitude)).json()['current'])
    except (exceptions.JSONDecodeError, KeyError) as e:
        return f'get {e.__class__.__name__}'


def get_weather_code(code: int) -> str:
    'Функция получения погоды по коду'
    return [v for k, v in CODES.items() if code in k][0]
