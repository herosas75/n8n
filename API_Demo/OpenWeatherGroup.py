from typing import NamedTuple, Optional, Dict

class WeatherCondition(NamedTuple):
    code: int
    group: str         # e.g. "Thunderstorm", "Clear", etc.
    main: str          # the broader category e.g. "Rain", "Snow", etc.
    description: str   # human-friendly description
    icon_base: str     # base icon identifier (like "10", "11", etc.), ignoring day/night, or the full icon code

# Build the mapping

_WEATHER_CONDITIONS: Dict[int, WeatherCondition] = {
    # Group 2xx: Thunderstorm
    200: WeatherCondition(200, "Thunderstorm", "Thunderstorm", "thunderstorm with light rain", "11"),
    201: WeatherCondition(201, "Thunderstorm", "Thunderstorm", "thunderstorm with rain", "11"),
    202: WeatherCondition(202, "Thunderstorm", "Thunderstorm", "thunderstorm with heavy rain", "11"),
    210: WeatherCondition(210, "Thunderstorm", "Thunderstorm", "light thunderstorm", "11"),
    211: WeatherCondition(211, "Thunderstorm", "Thunderstorm", "thunderstorm", "11"),
    212: WeatherCondition(212, "Thunderstorm", "Thunderstorm", "heavy thunderstorm", "11"),
    221: WeatherCondition(221, "Thunderstorm", "Thunderstorm", "ragged thunderstorm", "11"),
    230: WeatherCondition(230, "Thunderstorm", "Thunderstorm", "thunderstorm with light drizzle", "11"),
    231: WeatherCondition(231, "Thunderstorm", "Thunderstorm", "thunderstorm with drizzle", "11"),
    232: WeatherCondition(232, "Thunderstorm", "Thunderstorm", "thunderstorm with heavy drizzle", "11"),
    # Group 3xx: Drizzle
    300: WeatherCondition(300, "Drizzle", "Drizzle", "light intensity drizzle", "09"),
    301: WeatherCondition(301, "Drizzle", "Drizzle", "drizzle", "09"),
    302: WeatherCondition(302, "Drizzle", "Drizzle", "heavy intensity drizzle", "09"),
    310: WeatherCondition(310, "Drizzle", "Drizzle", "light intensity drizzle rain", "09"),
    311: WeatherCondition(311, "Drizzle", "Drizzle", "drizzle rain", "09"),
    312: WeatherCondition(312, "Drizzle", "Drizzle", "heavy intensity drizzle rain", "09"),
    313: WeatherCondition(313, "Drizzle", "Drizzle", "shower rain and drizzle", "09"),
    314: WeatherCondition(314, "Drizzle", "Drizzle", "heavy shower rain and drizzle", "09"),
    321: WeatherCondition(321, "Drizzle", "Drizzle", "shower drizzle", "09"),
    # Group 5xx: Rain
    500: WeatherCondition(500, "Rain", "Rain", "light rain", "10"),
    501: WeatherCondition(501, "Rain", "Rain", "moderate rain", "10"),
    502: WeatherCondition(502, "Rain", "Rain", "heavy intensity rain", "10"),
    503: WeatherCondition(503, "Rain", "Rain", "very heavy rain", "10"),
    504: WeatherCondition(504, "Rain", "Rain", "extreme rain", "10"),
    511: WeatherCondition(511, "Rain", "Rain", "freezing rain", "13"),
    520: WeatherCondition(520, "Rain", "Rain", "light intensity shower rain", "09"),
    521: WeatherCondition(521, "Rain", "Rain", "shower rain", "09"),
    522: WeatherCondition(522, "Rain", "Rain", "heavy intensity shower rain", "09"),
    531: WeatherCondition(531, "Rain", "Rain", "ragged shower rain", "09"),
    # Group 6xx: Snow
    600: WeatherCondition(600, "Snow", "Snow", "light snow", "13"),
    601: WeatherCondition(601, "Snow", "Snow", "snow", "13"),
    602: WeatherCondition(602, "Snow", "Snow", "heavy snow", "13"),
    611: WeatherCondition(611, "Snow", "Snow", "sleet", "13"),
    612: WeatherCondition(612, "Snow", "Snow", "light shower sleet", "13"),
    613: WeatherCondition(613, "Snow", "Snow", "shower sleet", "13"),
    615: WeatherCondition(615, "Snow", "Snow", "light rain and snow", "13"),
    616: WeatherCondition(616, "Snow", "Snow", "rain and snow", "13"),
    620: WeatherCondition(620, "Snow", "Snow", "light shower snow", "13"),
    621: WeatherCondition(621, "Snow", "Snow", "shower snow", "13"),
    622: WeatherCondition(622, "Snow", "Snow", "heavy shower snow", "13"),
    # Group 7xx: Atmosphere
    701: WeatherCondition(701, "Atmosphere", "Atmosphere", "mist", "50"),
    711: WeatherCondition(711, "Atmosphere", "Atmosphere", "smoke", "50"),
    721: WeatherCondition(721, "Atmosphere", "Atmosphere", "haze", "50"),
    731: WeatherCondition(731, "Atmosphere", "Atmosphere", "sand/dust whirls", "50"),
    741: WeatherCondition(741, "Atmosphere", "Atmosphere", "fog", "50"),
    751: WeatherCondition(751, "Atmosphere", "Atmosphere", "sand", "50"),
    761: WeatherCondition(761, "Atmosphere", "Atmosphere", "dust", "50"),
    762: WeatherCondition(762, "Atmosphere", "Atmosphere", "volcanic ash", "50"),
    771: WeatherCondition(771, "Atmosphere", "Atmosphere", "squalls", "50"),
    781: WeatherCondition(781, "Atmosphere", "Atmosphere", "tornado", "50"),
    # Group 800: Clear
    800: WeatherCondition(800, "Clear", "Clear", "clear sky", "01"),
    # Group 80x: Clouds
    801: WeatherCondition(801, "Clouds", "Clouds", "few clouds: 11-25%", "02"),
    802: WeatherCondition(802, "Clouds", "Clouds", "scattered clouds: 25-50%", "03"),
    803: WeatherCondition(803, "Clouds", "Clouds", "broken clouds: 51-84%", "04"),
    804: WeatherCondition(804, "Clouds", "Clouds", "overcast clouds: 85-100%", "04"),
}

def get_condition(code: int) -> Optional[WeatherCondition]:
    """Return the WeatherCondition corresponding to the given code, or None if unknown."""
    return _WEATHER_CONDITIONS.get(code)

def get_icon_url(code: int, is_day: bool = True) -> Optional[str]:
    """
    Construct the icon URL for a given weather code.
    OpenWeatherMap uses icons like "10d", "10n" etc.
    `is_day` determines if it's "d" or "n".
    Returns None if code unknown.
    """
    cond = get_condition(code)
    if cond is None:
        return None
    suffix = "d" if is_day else "n"
    # They use: https://openweathermap.org/img/wn/{icon_code}{suffix}@2x.png
    # Icon base is e.g. "10" or "11", etc.
    return f"https://openweathermap.org/img/wn/{cond.icon_base}{suffix}@2x.png"

def get_group(code: int) -> Optional[str]:
    """Return the group name for the code, e.g. 'Rain', 'Clouds', etc."""
    cond = get_condition(code)
    return cond.group if cond else None
