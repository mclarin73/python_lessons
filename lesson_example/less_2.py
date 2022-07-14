# Lesson 2
from random import randint
import os


# Slide 4
# Task 1
def odd_or_even(number: int) -> str:
    return 'Even' if number % 2 == 0 else 'Odd'


# Task 2
def shape_parameters(figure: str, area: float) -> str:
    figure = figure.lower()
    if figure == 'circle':
        return 'Big' if area > 100 else 'Small'
    elif figure == 'rectangle':
        return 'Big' if area > 100 else 'Small'
    elif figure == 'triangle':
        return 'Big' if area > 100 else 'Small'
    elif figure == 'square':
        return 'Big' if area > 100 else 'Small'
    else:
        print("Try again! Can't find figure")


# Task 3
def operation_with_numbers(numbers1: int, numbers2: int, operation: str) -> float:
    if operation == '+':
        return f'{numbers1} + {numbers2} = {numbers1 + numbers2}'
    elif operation == '-':
        return f'{numbers1} - {numbers2} = {numbers1 - numbers2}'
    elif operation == '*':
        return f'{numbers1} * {numbers2} = {numbers1 * numbers2}'
    elif operation == '/':
        return f'{numbers1} / {numbers2} = {numbers1 / numbers2 if numbers2 != 0 else 0.0}'


# Slide 7
# Task 1
def plus_user_number():
    try:
        first_value = int(input('Enter first value: '))
        second_value = int(input('Enter second value: '))
        return first_value + second_value
    except TypeError:
        return 'You enter string!'


# Slide 9
# Task 1
def calculate_task():
    score = 0
    all_task = 0

    start = input('Enter if you want play enter yes/no: ')
    while start != 'no':
        a = randint(0, 100)
        b = randint(0, 150)
        res = int(input(f'{a} + {b} = '))
        if res == a + b:
            print('U done!')
            score += 1
        else:
            print('Wrong answer')
        all_task += 1
        start = input('Enter anything to continue or no to stop: ')
    return f'You have  {score * 100 / all_task} % of all answer'


# Slide 10
# Task 1
def reverse_number(number: str) -> str:
    return str(number)[::-1] if len(str(number)) > 0 else 1


# Slide 24
# Task 1
def calculate_ten_numbers() -> float:
    res = []
    while len(res) != 10:
        try:
            input_number = int(input('Enter number: '))
            res.append(input_number)
        except TypeError:
            pass
    return sum(res) / len(res)


# Task 2
def multiples_of_14() -> list:
    return [i for i in range(1, 1001) if i % 14 == 0]


# Task 3
def prime_check(number: int) -> str:
    if str(number)[-1] in ['0', '2', '4', '5', '6', '8'] and number != 5:
        return f'{number} is not prime'
    else:
        for i in range(2, 101):
            if number % i == 0 and i != number:
                return f'{number} is not prime'
    return f'{number} is prime'


# Task 4
def graduate_student() -> None:
    student_dict = dict()
    input_val = input('For start enter anything:  ')
    while input_val != 'stop':
        name_of_student = input('Enter name of student: ')
        mark_of_student = input(f'Enter mark of {name_of_student}: ')
        try:
            student_dict[name_of_student] = int(mark_of_student)
        except TypeError:
            print('Try again!')
            os.system('cls')
        input_val = input('For stop enter stop:  ')

    avg = sum(student_dict.values()) / len(student_dict)
    for key, value in student_dict.items():
        if value >= avg:
            print(f'Student {key} have mark: {value} it is more than avg {avg}')
        else:
            print(f'Student {key} have mark: {value} it is less than avg {avg}')


# Slide 25
# Task 5-6-7
def square() -> None:
    # task 5
    for i in range(9):
        print('*' * 8)

    # task 6
    for i in range(9):
        print('#' * 8)

    # task 7
    for i in range(11, 0, -1):
        print('%' * i)

# Task 8
