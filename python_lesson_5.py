# Work with file system - mini pet  - continue 4 lessons

import requests
import datetime as dt


#start_prog = dt.datetime.now()

res = []
def div(number):
    #if number % 2 == 0: return True
    #else: return False
    return True if number % 2 == 0 else False


for i in range(1, 100):
    if len(res) == 15:
        break
    else:
        if div(i) == True:
            res.append(i)

print(res)

#end_prog = dt.datetime.now()


# Create simple weather-app
api_name = '33d99a1c99c5ea82e6aaff8592cd6fc3'
name_of_city = 'Lviv'



url_api = f'https://api.openweathermap.org/data/2.5/weather?q={name_of_city}&appid={api_name}&units=metric'
response = requests.get(url_api)
data_json = response.json()
