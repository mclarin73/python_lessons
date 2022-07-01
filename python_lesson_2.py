

# Task 1
# Building a fence
def building_fence(name_of_object:str, lenght:int) -> float:
    return 0.0


# Task 2
# Divisible by 3 or 5
def divisible_three_or_five(value:int):
    if value % 3 == 0 and value % 5 == 0:
        print('ham')
    elif value % 3 == 0:
        print('foo')
    elif value % 5 == 0:
        print('bar')
    else:
        print('no of Divisible')


# Task 3
# Work with error
def two_real_number():
    first_number = float(input('Enter first number: '))
    second_number = float(input('Enter second number: '))
    operation = input('Enter operation: ')
    if operation in ['+', '-', '/', '*']: # it is equal that: operation == '+' or operation == '-' or ...
        if operation == '+':
            print(first_number + second_number)
        elif operation == '-':
            print(first_number - second_number)
        elif operation == '*':
            print(first_number - second_number)
        elif operation == '/' and (first_number > 0 and second_number > 0):
            print(first_number / second_number)


# Task 4
# Avarage of ten values
def avarage_ten_values():
    list_of_number = []
    while len(list_of_number) != 10:
        input_number = int(input('Enter value:'))
        list_of_number.append(input_number)
    print(sum(list_of_number) // 10)


# Task 5
# All % of 14
def check_for_div():
    for i in range(1, 1001):
        if i % 14 == 0:
            print(i)


# Task 6
# Simple number
def simple_number(number:int):
    val = 0
    for i in range(2, 100):
        if number % i == 0 and number != i:
            print('No Prime')
            val += 1
            break
    if val == 0:
        print('Prime')


# Task 7
# Average of Student
def average_of_student():
    result = dict()
    stop_it = 'no'
    while stop_it != 'stop':
        name_of_student = input('Enter name of Student: ')
        mark_of_student = int(input('Enter mark: '))
        result[name_of_student] = mark_of_student
        stop_it = input('If you want to continue press any letter/ if you want to stop enter - stop: ')
    average = sum(result.values()) // len(result.keys())
    for i in result.keys():
        if result[i] >= average:
            print(f'Student {i}, have {result[i]} it is above average: {average}')
        else:
            print(f'Student {i}, have {result[i]} it is below average: {average}')


# Task 8
# Square of size 8*8
def build_square():
    # Variant 1
    pattern = '*' # Or write * points
    for i in range(7):
        pattern = pattern + '*'
    for i in range(8):
        print(pattern)


print(build_square())