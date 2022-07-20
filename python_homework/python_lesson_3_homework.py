# 3 - HW
# import all module that we need
from math import sqrt


# Task 1


# Task 2
# Professor Exam - лучше решать через класс
def professor_exam() -> None:

    # Функция помощник для очистки данных
    def helper_to_clean(items: str) -> str:
        return ''.join(i for i in items if i.isalpha()).capitalize() if items.isdigit() == False else ''.join(i for i in items if i.isdigit() == True)

    # Create helper func to take input from user
    # Хочу что б код можно было использовать три раза, поэтому мы сами будем
    # Передавать параметр для ввода, y нас будет student, mark, result_of_exam
    def helper_func_input(parameter_to_input='student') -> list:
        res = []
        input_desc = input('If you want to start enter yes/no: ')
        while input_desc != 'no':
            text_input = input(f'Write you info about {parameter_to_input}: ')
            res.append(helper_to_clean(text_input))
            input_desc = input('If you want to stop enter no: ')
        return res

    student = helper_func_input('student')
    mark = helper_func_input('mark')
    result_of_exam = helper_func_input('result_of_exam')
    result = list(zip(student, mark, result_of_exam))

    for value in result:
        print(f'Student {value[0]} have mark {value[1]} and he {value[2]} exam')


# Task 3
# Scope task with formula
def scope_task(arr: list) -> list:
    mean_arr = sum(arr) / len(arr)  # calculate mean
    std_arr = sqrt(mean_arr)
    # First variant
    res = []
    for i in arr:
        res.append(round((i - mean_arr) / std_arr, 2))
    # return res

    # Second variant
    return [round((i - mean_arr) / std_arr, 2) for i in arr]
