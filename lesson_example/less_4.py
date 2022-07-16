# Lesson 4
from python_lessons.lesson_example.less_2 import prime_check


# Slade 13
# Task 1
def find_prime() -> list:
    return [i for i in range(1, 1001) if prime_check(i) == f'{i} is prime']
