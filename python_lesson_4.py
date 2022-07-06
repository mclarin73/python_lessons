# Lesson 3 end and Lesson 4

# import frame
import random

#def test(a):
#    return True if a >= 18 and a <= 27  else False
arr = [1,3,5,7,90, -1]
#print(sum(arr), max(arr), min(arr))
counter = 0
max_of = 0
min_of = 0

#for i in arr:
#    if i > max_of:
#        max_of = i
#    elif i < min_of:
#        min_of = i
#    counter += i
#print(counter, max_of, min_of)
# [::-1] == reversed

#print(random.randint(1,10))
def mean(x:list) -> float:
    return sum(x) / len(x)


def summ_of(arr:list) -> float:
    couter = 0
    for i in arr:
        couter += i
    print(couter)
    return sum(arr)

#print(summ_of([4,5,7,2,9]))
#mean_a = mean([12,4,6,8])
#print(mean((3,4,6,7)))

# Desc: (arr - tuple) -> list, divide of 2
def dive_of(arr):
    # First Variant
    res = []
    for i in arr:
        if i % 2 == 0:
            res.append(i)
    # Second Variant
    return [i for i in arr if i % 2 == 0]


def func_for_func() :
    return None


def hello_name(name:str = 'Oleksandr', surname:str = 'Test'):
    return 'Hello ' + name + ' ' + surname +'\nHave a good day!'

#print(hello_name())
#print(dive_of(list(range(1,51))))


mean_lambda = lambda x: sum(x) / len(x)
summ_lambda = lambda x: sum(x)
plus_lambda = lambda a,b: a + b

list_of_number = [3,4,6,7,2, 5]
def print_hello_world():
    print('Hello World!')

#print(mean_lambda(list_of_number))
#print(plus_lambda(5,5))
student = [5,6,7,1,3,5]
mean_of_user_mark = mean(student)
#for i in student:
#    if i > mean_of_user_mark:
#        print('Big', i)
#    elif i < mean_of_user_mark:
#       print('Small', i)#
#       elif i == mean_of_user_mark:
#       print('Eval', i)

# zip func
first_a = [1, 2, 3, 4,5]
second_b = ['a', 'b', 'c', 'e', 'e','e']
third = [1,34,5,6, 6,6]
if len(first_a) == len(second_b) == len(third):
    result = list(zip(first_a, second_b, third))
    res = []
    for i in result:
        res.append(list(i))
    print(res)
else:
    print('Add new elemnt')

#print(summ_lambda(mean_lambda([1,3,4,6,9])))
