import requests
           
API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

user_input = input('Enter City: ')

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={API_KEY}"
    ,timeout=5)

weather = weather_data.json()['weather'][0]['main']

temp =  (weather_data.json()['main']['temp'])

temp2 = round((temp-32)*(5/9))

print(f"The Weather In {user_input} Is: {weather}")
print(f"The Temperature In {user_input} Is: {temp2}ºC")
