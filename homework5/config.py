TOKEN = "6808702668:AAEIWt2V7mzdWADpuD0eyR6ji79ipi_ZWTQ" # Вставить токен
URL = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m,wind_direction_10m,wind_gusts_10m&timezone=Europe%2FMoscow&forecast_days=1" # Ссылка для API запросов
SEND_PLEASE = "Пришлите пожалуйста свое местоположение для определения погоды" # Ответ на команду /weather
WEATHER_INFO = "⌚ <b>{}</b>\n🌡️ Температура: {} °C\n🌡️ Чувствуется как: {} °C\n💧 Влажность воздуха: {}%\n☁️ Облачно на {}%\n🪁 Скорость ветра: {} км/ч\n{}" # Информация о погоде
CODES = { # Информация о кодах погоды
    (0,): "☀️ Ясно", 
    (1, 2, 3,): "🌥️ Пасмурно", 
    (45, 48,): "🌫️ Туман", 
    (51, 53, 55,): "☁️ Морось",
    (56, 57,): "🌧️ Моросящий дождь",
    (61, 63, 65,): "🌧️ Дождь",
    (66, 67,): "🧊 Ледяной Дождь",
    (71, 73, 75,): "🌨️ Снегопад",
    (77,): "🌨️ Град",
    (80, 81, 82,): "🌧️ Ливень",
    (85, 86,): "❄️ Метель",
    (95,): "🌩️ Гроза",
    (96, 99,): "⛈️ Гроза с градом"
}