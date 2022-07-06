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

#print(dive_of(list(range(1,51))))