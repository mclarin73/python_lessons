# Lesson 4
from python_lessons.lesson_example.less_2 import prime_check

# Slade 13
# Task 1
def find_prime() -> list:
    return [i for i in range(1,1001) if prime_check(i) ==  f'{i} is prime']


# Task 1
#def grade_of_student() -> None:
#   result = dict()
 #   start_program = input('Start program enter yes/no: ')

 #   while start_program != 'stop':
 #       student_names = input('Enter name of student by ,: ').lstrip(' ').rstrip(' ').split(',')
  #      grade_student = input('Enter grade of student by ,: ').lstrip(' ').rstrip(' ').split(',')
 #       start_program = input('Stop program enter stop: ')
 #       helper = zip(student_names, grade_student)


