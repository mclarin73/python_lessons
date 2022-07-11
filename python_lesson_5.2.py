# filter map reduce
from functools import  reduce


def plus_two_value(a, b):
    return a + b


def div_value(item):
    return True if item % 2 == 0 else False


def change_minus(item):
    return item * -1


def check_string(item):
    return True if item in ['a', 'b', 'c'] else False


string = 'ardbc'
print(list(filter(check_string, string)))

a = list(range(10))
b = list(filter(div_value, a))
c = list(filter(lambda x: x % 2 == 1, a))
#print(b)
#print(c)

a_map = list(range(-10, 10))
print(a_map)
b_map = list(map(change_minus, a_map))
c_map = list(map(lambda x: x ** 2, a_map))
print(b_map)
print(c_map)

a_reduce = [14,5,7,8,3,4,12, 68, -10]
string_reduce = ['s', 'a', 's', 'c', 'h', 'a']

b_reduct = reduce(lambda x, y: x + y, a_reduce)
c_reduce = reduce(lambda x, y: x + y, string_reduce)
d_reduct = reduce(plus_two_value,string_reduce )
print(c_reduce)
print(d_reduct)