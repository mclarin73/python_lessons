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

new_data = json.loads(str_json) # create from JSON to dict

print(new_data.keys()) # посмотреть верхний ключ
print(new_data['Student1'].keys()) # посмотреть все значение по ключу

for upper_level_json in new_data.keys(): # пара ключ-значение можно пройти в цикле for/while
    for key, value in new_data[upper_level_json].items(): # пройдемся по вложенных значений
        print(f'{upper_level_json} хранит в себе ключ {key} у которого значение {value}')


