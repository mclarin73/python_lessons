from collections import defaultdict, Counter
from itertools import product, permutations
class Transport:
    """
    class desc transport type
    """
    def __init__(self, name, wei, mark):
        self.name = name
        self.wei = wei
        self.mark = mark

    def calculate(self):
        return self.wei ** 2

    def print_info(self):
        return f'Hello {self.name} u strong {self.mark}'



obj_a = Transport(name= 'Bus',wei=4000, mark='Bogdan')
#print(obj_a.print_info())
#print(obj_a.name)
#print(obj_a.wei)
#print(obj_a.mark)
#print(obj_a.calculate())

obj_b = Transport(name='Train', wei=30000, mark='Hundai')
#print(obj_b.print_info())

#input_some_text = input('Enter name: ')
input_some_text = 'Vadimm'
name_list = ['sasha', 'sasha', 'sasha', 'Sasha', 'vadim', 'maria', 'maria']
some_r = [1,2 ,3,4,5]
counter = dict(Counter(input_some_text))
#print(counter.most_common(3))
#print(Counter(some_r))
#print(Counter(name_list))
print(list(product(some_r, name_list)))

dna = 'abc'
print(list(permutations(dna)))
