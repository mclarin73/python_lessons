# Lesson 2
import random


a = 5

age = 18
a_for_rand = 1
test_on_rand = random.randint(a_for_rand, 11)
# True and True and ...
# True or True
if test_on_rand >= age and test_on_rand % 2 == 0: # condin = True/False
    pass
elif test_on_rand >= age and test_on_rand % 2 == 1:
    pass
else:
    pass

# Child if age age < 5
if test_on_rand > 0 and test_on_rand < 5:
    print('Child', test_on_rand)
elif test_on_rand >= 5:
    print('Pre-school', test_on_rand)

# 3 5 7 9 11 13 17
# 3-1 = 2 3 + 1 = 4
first_value = int(input('Enter first value: '))
second_value = int(input('Enter second value: '))
operation = input('Enter operation: ')

# + , - , *, /
if operation == '+':
    if first_value > 150:
        first_value = random.randint(0, 100)
        print(first_value + second_value)
elif operation == '-':
    print(first_value - second_value)
elif operation == '*' and int(first_value) // 2:
    print(first_value * second_value)
elif operation == '/' and second_value != 0 and first_value != 0:
    print(first_value / second_value)
    #if second_value != 0:
    #   print('df')
    # elif second_value == 0:
    #    if second_value % 2 == 3:
else:
    print('No command')

