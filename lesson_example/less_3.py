print('Lesson 3')
from  functools import reduce

# Slide 5. Task-1
def factor_of_number(number: int) -> list:

    helper_to_mul = 0
    first_value = number
    pattern = [2,3,5, 7]
    res = []
    while helper_to_mul != first_value:
        for i in pattern:
            if number % i == 0:
                number //= i
                res.append(i)

        helper_to_mul = reduce(lambda x,y: x * y, res)

    return res


# Slide 7
# Task 1
