print('Init hello')


# Task 1
# Seconds in a day
def second_in_day() -> int:
    return 60 * 60 * 24


# Task 2
# Seconds in a year
# First part it is calculate seconds in day and then to multiply for one year with 365 days
def second_in_year() -> int:
    return (60 * 60 * 24) * 365


# Task 3
# New Planet
def planet_name() -> str:
    return 'String'


# Task 4
# Person Age
def person_age(data_in_mouth:int) -> bool:
    constant_over_18_mounth = 18 * 12
    # Variant 1
    if data_in_mouth >= constant_over_18_mounth:
        return True
    else:
        return False
    # Variant 2
    # return True if data_in_mouth >= constant_over_18_mounth else False


# Task 5
# Rectangle task
def rectangle_task(height:int, weight:int) -> int:
    return 'Area : {0} \nPerimeter : {1}'.format(height * weight, 2 * (height + weight))


# Task 6
# Even or not even
def even_value(value:int) -> str:
    # Variant 1
    if value % 2 == 0:
        return 'True'
    else:
        return 'False'
    # Variant 2
    #return 'True' if value % 2 == 0 else 'False'


