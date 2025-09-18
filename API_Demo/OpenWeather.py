from fastapi import FastAPI
import requests
import OpenWeatherGroup

app = FastAPI()

weather = {
    "locationName": "",
    "temp": 0,
    "humidity": 0,
    "groupDescription": "",
    "iconURL" : ""
}

@app.get("/myapi/weather")
def get_weather(lat, lon, API_KEY):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    item = requests.get(url.format(lat=lat, lon=lon, API_KEY= API_KEY)).json()

    weather['locationName'] = item["name"]
    weather['temp'] = item["main"]["temp"]
    weather['humidity'] = item["main"]["humidity"]

    condition = item["weather"][0]["id"]
    group = OpenWeatherGroup.get_condition(condition)
    icon = OpenWeatherGroup.get_icon_url(condition)

    weather['groupDescription'] = group.description
    weather["iconURL"] = icon

    return weather
