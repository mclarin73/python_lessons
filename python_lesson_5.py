# Work with file system - mini pet  - continue 4 lessons

import requests
import json
import datetime as dt


#start_prog = dt.datetime.now()

res = []
def div(number):
    #if number % 2 == 0: return True
    #else: return False
    return True if number % 2 == 0 else False


#for i in range(1, 100):
#    if len(res) == 15:
#        break
#    else:
#       if div(i) == True:
#       res.append(i)

# print(res)

#while True:
   # input_value = input('enter quit if u want stop: ')
  #  if input_value == 'quit':
   #     break
   # else:
   #     print(input_value)


#input_value = input('enter quit if u want stop: ')
#while input_value != 'quit':
#    input_value = input('enter quit if u want stop: ')
 #   print(input_value)

def check_div_and_cont(enter_range:int, val = 0) -> None:
    # some cond
    for i in range(int(enter_range)):
        if i % 2 == 0:
            continue
        else:
            print(i, val)

#print(check_div_and_cont(enter_range=10, val=2))
#print(sorted([1,3,5,6], reverse=False))
#a = check_div_and_cont(100)
#print(type(a))
# print(check_div_and_cont(100.5))

#for i in range(0, 100):
#    if i % 2 == 1:
#        pass
#    else:
#        print(i)
def args_example(*args):
    help_list = list(args)
    print(type(args))
    for i in help_list:
        print(i)

#print(args_example(*(5,3,5)), args_example([12, [1,3,4],4,6,7,8,9,12]))

#end_prog = dt.datetime.now()

#f = open('new_file.txt', 'x') # создание файла
f = open('/Users/alksandr/Desktop/test.txt', 'a')

f.write('Some text')
f.close()

f = open('/Users/alksandr/Desktop/test.txt', 'r')
#print(f.read())
f.close()

#f = open('/Users/alksandr/Desktop/d.txt', 'r')
#print(f.read())
#f.close()
#with open('/Users/alksandr/Desktop/d.txt', 'r') as f:
 #   print(type(f.readline()))

# RLE
# AAAABBB -> A4B3

obj = {'name': 'Arthur Conan Doyle',
       'books': [{'name': 'The Hound of the Baskervilles'},
                 {'name': 'The Leather Funnel'}]}
print(obj.keys())
print(obj['name'], obj['books'])
for i in obj['books']:
    print(i)

#a_input = input('Enter value:')
#b_input = input('Enter second value: ')

#try:
#    a_input = int(a_input)
#    b_input = int(b_input)
#    print(a_input / b_input)
#except:
    #print('No Value')
#    print('Try Again!')
#else:
#    print(a_input)




# Create simple weather-app



def check_input_city(name:str) -> str:
    # First Variant
    return ''.join(i for i in name if i.isalpha() or i in [' ', '-']).capitalize()
    # Second Variant
    # res = ''
    #for i in name:
    #    if i.isalpha() or i in [' ', '-']:
            # res = res + i
            # .... save in result


def get_weather(name:str, api:str):
    try:
        url_api = f'https://api.openweathermap.org/data/2.5/weather?q={name_clear}&appid={api_name}&units=metric'
        response = requests.get(url_api)
        data_json = response.json()
        return data_json['main']['temp']
    except:
        print('Wrong name api, or wrong name city')

api_name = '33d99a1c99c5ea82e6aaff8592cd6fc3'
des_input = input('Enter something to continue else enter stop: ')
while des_input != 'stop':

    name_of_city = input('Input City:')
    name_clear = check_input_city(name_of_city)
    print(f'Weather in city {name_clear} is {get_weather(name_clear, api= api_name)}')
    des_input = input('Enter something to continue else enter stop: ')

