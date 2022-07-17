# Lesson 5


# Slide 7
# Task 1


# Slide 10
# Task 1
def long_number() -> None:
    res = []
    start = input('Enter anything to start:')
    while start != 'stop':
        try:
            input_number = int(input('Enter number: '))
            res.append(input_number)
        except ValueError:
            print('You write not a number, try again')
        start = input('Enter stop to stop or anything to continue:')
    print(res)


# Slide 13
# Task 1
def mark_more_than(array_of_student: str, array_of_mark: str) -> str:
    result_string = ''
    helper_list = []
    try:
        for i in array_of_mark.split(','):
            helper_list.append(int(i))
    except ValueError:
        pass

    result = dict(zip(array_of_student.split(','), helper_list))

    for key, value in {key: value for key, value in result.items() if value > 90}.items():  # Try to split
        result_string = result_string + f'Student {key} have mark {value}\n'

    return result_string


# Slide 18
# Task 1
def power_rec(a: int, b: int) -> int:
    if b == 0:
        return 1
    if b % 2 == 0:
        return power_rec(a, b // 2) * power_rec(a, b // 2)
    else:
        return power_rec(a, b - 1) * a
