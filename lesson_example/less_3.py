# Lesson  3

from functools import reduce
import numpy as np
from random import randint


# Slide 5. Task 1
def factor_of_number(number: int) -> list:
    helper_to_mul = 0
    first_value = number
    pattern = [2, 3, 5, 7]
    res = []
    while helper_to_mul != first_value:
        for i in pattern:
            if number % i == 0:
                number //= i
                res.append(i)

        helper_to_mul = reduce(lambda x, y: x * y, res)

    return res


# Slide 7
# Task 1


# Task 2
def mark_student() -> None:
    name_and_mark = dict()
    enter_name = input('Enter you name: ')
    start = input('Enter anything to start or write stop: ')
    while start != 'stop':
        write_name = input('Enter name of teacher: ')
        mark = input('Enter marks with ,: ')  # Через запятую вводит все свои оценки
        name_and_mark[write_name] = mark.lstrip(' ').rstrip(' ').split(',')
        start = input('Enter anything to start or write stop: ')

    for key, value in name_and_mark.items():
        print(
            f'Student: {enter_name}\nWith teacher {key} you have medium value is {sum([int(i) for i in value if i.isdigit()]) / len(value)}')


# Slide 19
# Task 1
def chess_tournament() -> dict:
    pass


# Task 2
def math_func() -> None:
    operation = ['+', '-', '*', '/']
    res = dict()

    # Helper func to generate value
    def help_to_random_operator() -> list:
        return [randint(0, 1000), randint(0, 1001)]

    # Helper func to random operation
    def choose_operation(item1: int, item2: int) -> str:
        return operation[randint(0, 3)] if item2 != 0 else operation[randint(0, 3)]

    # Except for wrong type
    def helper_try(item: str) -> int:
        try:
            return int(item)
        except TypeError:
            return 0

    input_des = input('Enter anything to start or stop to stop: ')

    while input_des != 'stop':
        tmp_operation = help_to_random_operator()
        if choose_operation(tmp_operation[0], tmp_operation[1]) == '+':
            user_variant = input(f'Enter {tmp_operation[0]} + {tmp_operation[1]} = : ')
            if helper_try(user_variant) == sum(tmp_operation):
                res[f'{tmp_operation[0]} + {tmp_operation[1]} = {sum(tmp_operation)}'] = f'You answer correct! {user_variant} '
            else:
                res[f'{tmp_operation[0]} + {tmp_operation[1]} = {sum(tmp_operation)}'] = f'You answer wrong {user_variant} :( '

        elif choose_operation(tmp_operation[0], tmp_operation[1]) == '-':
            user_variant = input(f'Enter {tmp_operation[0]} - {tmp_operation[1]} = : ')
            if helper_try(user_variant) == tmp_operation[0] - tmp_operation[1]:
                res[f'{tmp_operation[0]} - {tmp_operation[1]} = {tmp_operation[0] - tmp_operation[1]}'] = f'You answer correct! {user_variant}'
            else:
                res[f'{tmp_operation[0]} - {tmp_operation[1]} = {tmp_operation[0] - tmp_operation[1]}'] = f'You answer wrong {user_variant} :('

        elif choose_operation(tmp_operation[0], tmp_operation[1]) == '*':
            user_variant = input(f'Enter {tmp_operation[0]} * {tmp_operation[1]} = : ')
            if helper_try(user_variant) == tmp_operation[0] * tmp_operation[1]:
                res[f'{tmp_operation[0]} * {tmp_operation[1]} = {tmp_operation[0] * tmp_operation[1]}'] = f'You answer correct! {user_variant}'
            else:
                res[f'{tmp_operation[0]} * {tmp_operation[1]} = {tmp_operation[0] * tmp_operation[1]}'] = f'You answer wrong {user_variant} :('

        elif choose_operation(tmp_operation[0], tmp_operation[1]) == '/':
            user_variant = input(f'Enter {tmp_operation[0]} / {tmp_operation[1]} = : ')
            if helper_try(user_variant) == tmp_operation[0] / tmp_operation[1]:
                res[f'{tmp_operation[0]} / {tmp_operation[1]} = {tmp_operation[0] / tmp_operation[1]}'] = f'You answer correct! {user_variant}'
            else:
                res[f'{tmp_operation[0]} / {tmp_operation[1]} = {tmp_operation[0] / tmp_operation[1]}'] = f'You answer wrong {user_variant} :('

        input_des = input('Enter anything to start or stop to stop: ')

    return res


# Slide 20
# Task 1
def std(arr: list) -> float:
    med = sum(arr) / len(arr)
    help_arr = sum([(i - med) ** 2 for i in arr]) // len(arr)
    return f'Numpy return {np.std(arr)}\nOur function return {help_arr ** 0.5}'
