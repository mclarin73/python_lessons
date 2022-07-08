# Work with file system
import requests






# Create simple weather-app
api_name = '33d99a1c99c5ea82e6aaff8592cd6fc3'
name_of_city = 'Lviv'



url_api = f'https://api.openweathermap.org/data/2.5/weather?q={name_of_city}&appid={api_name}&units=metric'
response = requests.get(url_api)
data_json = response.json()
