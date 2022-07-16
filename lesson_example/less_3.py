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
def tennis_tournament() -> None:
    counter = 1
    first_name = input('Enter name of first player: ').capitalize()
    second_name = input('Enter name of second player: ').capitalize()
    result = {first_name: 0, second_name: 0}
    while counter != 11:
        res_of_round = input(f'Round: {counter}, this round win: {first_name} or {second_name}: ').capitalize()

        if res_of_round in [first_name, second_name]:
            if res_of_round == first_name:
                result[first_name] += 1
            else:
                result[second_name] += 1
            counter += 1
        else:
            print('You write wrong name. Try again!')
    return f'{first_name} win {second_name} with score: {result[first_name]}' if result[first_name] > result[second_name] else f'{second_name} win {first_name} with score: {result[second_name]}'


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
    name_with_win = []
    win_dict = dict()

    def helper_check_user_enter(value):
        try:
            return int(value)
        except TypeError:
            return 'Sorry, try again!'

    start_value = input('Enter how many members in tournament: ')

    if helper_check_user_enter(start_value):
        start_value = helper_check_user_enter(start_value)
        for i in range(start_value):
            enter_name = input('Enter name of user: ').capitalize()
            if enter_name in name_with_win:
                name_with_win.append(enter_name + str(randint(0, 100)))
            else:
                name_with_win.append(enter_name)
    win_dict = {i: 0 for i in name_with_win}
    counter = 10
    help_to_iterate = 1
    start_tournament = name_with_win[0]

    while counter != 0:
        for i in range(0, len(name_with_win)):
            if name_with_win[i] != start_tournament:
                result = input(f'{start_tournament} vs {name_with_win[i]} who win: ').capitalize()
                if result in win_dict.keys():
                    if result == start_tournament:
                        win_dict[start_tournament] += 1
                    elif result == name_with_win[i]:
                        win_dict[name_with_win[i]] += 1
            else:
                continue
        try:
            start_tournament = name_with_win[help_to_iterate]
            help_to_iterate += 1
        except IndexError:
            break

    for key, value in sorted(win_dict.items()):
        if value > 0:
            print(f'Player {key} win {value} game')


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
