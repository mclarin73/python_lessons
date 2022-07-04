# Task 1
# Salary in year
def salary_in_year(name:str, salary:int) -> str:
    return name + "'s" + " yearly salary is "  + "$" + str(salary * 12 // 1000) + 'K.'


# Task 2
# Compare circle
def compare_circle(side_length: float, circle_radius: float) -> None:
    PI = 3.14
    # Variant 1
    if 2 * PI * circle_radius > side_length ** 2:
        print(True)
    else:
        print(False)
    # Variant 2
    #return True if 2 * PI * circle_radius  else False


# Task 3
# Check real number
def check_real_number():
    input_value = input('Enter value: ')
    if input_value.isdigit():
        print(True)
    else:
        print(False)


# Task 4
# Even number
def even_number():
    input_value = input('Enter value: ')
    if input_value.isdigit() or input_value.isdecimal():
        if int(input_value) % 2 == 0 and int(input_value) in range(100, 999):
            print(True)
    else:
        print(False)


# Task 5
# Reverse number
def reversed_number():
    # First Variant
    input_number = int(input('Enter number:'))
    # Second Variant
    #input_number = input('Enter number')
    #if input_number.isdecimal(): some do
    if input_number >= 101 and input_number <= 999:

        input_number = str(input_number)
        # First Variant
        print(input_number[::-1])
        # Second Variant
        #result = ''
        #for i in range(len(input_number), 0, -1):
        #    result += input_number[i-1]
        #print(result)
    else:
        print(input_number)


# Task 6
# Two integer
def two_integer():
    first_value = int(input('Enter first value: '))
    second_value = int(input('Enter second value: '))
    print(f'Sum: {first_value} + {second_value} = {first_value + second_value}')
    print(f'Diff: {first_value - second_value}')
    print(f'Product: {first_value*second_value}')
    print(f'Diff {first_value} by {second_value} is {first_value // second_value}')
    print(f'Part of by division {first_value % second_value}')
    print(first_value >= second_value)
