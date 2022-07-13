# Work with Json

import json

# Учебный JSON
str_json = '''
{  
    "Student1": {  
        "name":       "TestStudent1",   
        "salary":      1234567,   
        "married":    false  
    },
    "Student2": {
        "name":       "TestStudent2",   
        "salary":      56000,   
        "married":    true  
    }
} 
'''

new_data = json.loads(str_json) # Сreate from JSON to dict

print(new_data.keys()) #Посмотреть верхний ключ
print(new_data['Student1'].keys()) # Посмотреть все значение по ключу

for upper_level_json in new_data.keys(): # пара ключ-значение можно пройти в цикле for/while
    for key, value in new_data[upper_level_json].items(): # пройдемся по вложенных значений
        print(f'{upper_level_json} хранит в себе ключ {key} у которого значение {value}')


# Pickle
import pickle


# Создание и вписывание данных(шаг 1)
#name_with_mark = {'Name1': 90, 'Name2':98, 'Name3':60, 'Name4':76, 'Name5':81}

#pickle_out = open('dict.pickle', 'wb') # создать pickle
#pickle.dump(name_with_mark, pickle_out) # вписать в него значение словаря
#pickle_out.close() # закрыть файл

# После шага один(закоментировать код)
# Шаг два - разпаковка данных
pickle_in = open('dict.pickle', 'rb')
new_name = pickle.load(pickle_in) # создали словарь

print(new_name.keys()) # можно работать как с обычным словорем

for key in new_name.keys():
    print(key)
