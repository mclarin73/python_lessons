# Lesson  3
from functools import reduce


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
        print(f'Student: {enter_name}\nWith teacher {key} you have medium value is {sum([int(i) for i in value if i.isdigit()]) / len(value)}')
