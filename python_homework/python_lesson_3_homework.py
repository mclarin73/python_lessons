# 3 - HW
# import all module that we need
from math import sqrt

# Task 1


# Task 2
# Professor Exam
def professor_exam() -> None:
    # Create helper func to take input from user
    # Хочу что б код можно было использовать три раза, поэтому мы сами будем
    # Передавать параметр для ввода, y нас будет student, mark, result_of_exam
    result_dict = dict()
    pattern_of_input = ['student', 'mark', 'result_of_exam']
    def helper_func_input(parameter_to_input='student'):
        res = []
        input_desc = input('If you want to start enter yes/no: ')
        while input_desc != 'no':
            text_input = input(f'Write you info about {parameter_to_input}: ')
            res.append(text_input)
            input_desc = input('If you want to stop enter no: ')
        return res

    
print(professor_exam())


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
