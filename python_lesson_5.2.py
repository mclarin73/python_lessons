# filter map reduce

def div_value(item):
    return True if item % 2 == 0 else False

a = list(range(100))
b = list(filter(div_value, a))
c = list(filter(lambda x: x % 2 == 1, a))
print(b)
print(c)