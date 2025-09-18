This is a simple n8n demo to prove the custom API usage (HTTP Request) using python API (FastAPI).

Will get the Weather from OpenWeathermap and send a sms message, OpenWeather token is needed, to get it creata an account and go to APIs to get one.
Also latitude and longitude fro the place you want to send the message.

Also an account will be needed for Twilio to send the sms message t the desire cel number. Multiple options can be selected as example you can send this to an email too.

To run the FastAPI service in yout python file fodler run: uvicorn OpenWeather:app --reload
this will run the service under Uvicorn running on http://127.0.0.1:8000 so in n8n just point to this: http://127.0.0.1:8000/myapi/weather?lat=20.7167&lon=-103.4&API_KEY={key}
