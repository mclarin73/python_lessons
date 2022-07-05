# Build a Fence
# Task 1


# Task 2
# Check for divisible
def divisible():
    user_input = int(input('Enter value:'))
    if user_input % 3 == 0 and user_input % 5 == 0:
        print('ham')
    elif user_input % 3 == 0 and user_input % 5 != 0:
        print('foo')
    elif user_input % 5 == 0 and user_input % 3 != 0:
        print('bar')
    else:
        print("I don't know it")


# Task 3
# Which is larger
def larger_of_smaller():
    fisrt_user_number = int(input('Enter first value: '))
    second_user_number = int(input('Enter second value: '))
    # First variant
    if fisrt_user_number > second_user_number:
        print(f'{fisrt_user_number} is larger that {second_user_number} it is mean that\n {second_user_number} is smaller')
    else:
        print(f'{second_user_number} is larger that {fisrt_user_number} it is mean that\n {fisrt_user_number} is smaller')
    # Second variant
    #print( f'{fisrt_user_number} is larger that {second_user_number}' if fisrt_user_number >= second_user_number else f'{second_user_number} is larger that {fisrt_user_number}')


# Task 4
# equal value
def equal_value():
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))
    third_number = int(input('Enter third number: '))
    # First variant - не рекомендую, только учебный пример
    if first_number >= second_number and first_number >= third_number:
        print(f'{first_number} is larger value')
        if second_number >= third_number:
            print(f'{second_number} is medium value')
        elif third_number >= second_number:
            print(f'{third_number} is medium value')
        else:
            print(f'{third_number} is last element')
    elif second_number >= first_number and second_number >= third_number:
        print(f'{second_number} is larger value')
        if first_number >= third_number:
            print(f'{second_number} is medium value')
        else:
            print(f'{third_number}')
    elif third_number >= first_number and third_number  >= second_number:
        print(f'{third_number} is larger value')
        if first_number >= second_number:
            print(f'{first_number} is medium value')
        else:
            print(f'{second_number}')

    # Second variant - рекомендую
    help_list = sorted([first_number, second_number, third_number])[::-1]
    print(f'{help_list[0]} is larger number\n{help_list[1]} is medium number\n{help_list[-1]} is smaller value')


# Task 5 - Task 6
# rock paper scissors - game
import random
def rock_paper_scissors_game():
    result_user = 0
    result_computer = 0

    enter_value = input('For start game enter yes/no: ')
    # First Variant - Second variant to use dict
    # Можно значительно упростить, это учебный пример
    if enter_value == 'yes':
        while enter_value != 'no':
            typed_option  = int(input('For choose enter value 1 - rock, 2 - paper, 3 - scissors: '))
            option_computer = random.randint(1,3)
            if typed_option == option_computer:
                print('U both game, try again to win')
                result_user += 1
                result_computer += 1
                enter_value = input('Continue a game yes/no: ')

            elif typed_option == 1 and option_computer == 3:
                print('U win, computer option is scissors')
                result_user += 1
                enter_value = input('Continue a game yes/no: ')

            elif typed_option == 2 and option_computer == 1:
                print('U win, computer option is rock')
                result_user += 1
                enter_value = input('Continue a game yes/no: ')

            elif typed_option == 3 and option_computer == 2:
                print('U win, computer option is paper')
                result_user += 1
                enter_value = input('Continue a game yes/no: ')

            elif option_computer == 1 and typed_option == 3:
                print('U loose computer')
                result_computer += 1
                enter_value = input('Continue a game yes/no: ')

            elif option_computer == 2 and typed_option == 1:
                print('U loose computer')
                result_computer += 1
                enter_value = input('Continue a game yes/no: ')

            elif option_computer == 3 and typed_option == 2:
                print('U loose computer')
                result_computer += 1
                enter_value = input('Continue a game yes/no: ')
            else:
                print('Try again')
                enter_value = input('Continue a game yes/no: ')

    print(f'U win {result_user}\nComputer win {result_computer}')
    if result_user > result_computer:
        print(f'U win computer')
    elif result_computer > result_user:
        print(f'U loose computer :(')
    elif result_computer == result_user:
        print('Tie  with computer')
    else:
        print('Play next time, have a good day')


# Task 7
# sequence and detect smallest
def sequence():
    enter_des = input('If you want to start enter yes/no: ')
    smallest_number = 0
    while enter_des != 'no':
        enter_number = int(input('Enter value: '))
        if enter_number < smallest_number:
            smallest_number = enter_number
        enter_des = input('If you want to start enter yes/no: ')
    print('Smallest value is, ', smallest_number)

