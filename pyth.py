


#action = input('Enter dess:')
#while action != 'quit':
#    if action == 'greet':
#        print('Hello World!')
#    elif action == 'ask':
#        print('How are you?')
#    else:
#        print('All ok!')
#    action = input('Enter dess:')

# break, return, fallthrou

# index = 0
# Text = 0:T, 1:e, 2:x, 3:t
stroka = 'UkraineUA'
iterator = 0
# range(0..10)

while iterator != len(stroka):
    print(stroka[iterator])
    iterator += 1
# 1 step: print iterator 1++
# 2 step: print iterator 1++

number_string = '12345'# 1: 0, 2: 1, 3:2, 4: 3, 5:4
print(number_string[::])
iterator_for_len = len(number_string)
#while iterator_for_len != 0:
#    print(number_string[iterator_for_len])
#    iterator_for_len -= 1

print(number_string, number_string) # [start:end:step]

# Simple: int, float, bool, chr
# String, List
# Massiv = Array = List
some_list = list()
some_list.append(12)
some_list.append(16)
some_list.append(17)

some_list_1 = [23,54,78, 99, 0, True]
print(some_list, some_list_1[::])
print(some_list_1[0])

# print(some_list_1[0:some_list_1.index(0)])



