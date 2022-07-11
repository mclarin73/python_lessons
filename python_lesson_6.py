

class Transport:
    """
    class desc transport type
    """
    def __init__(self, name, wei, mark):
        self.name = name
        self.wei = wei
        self.mark = mark

    def print_info(self):
        return f'Hello {self.name} u strong {self.mark}'



obj_a = Transport(name= 'Bus',wei=4000, mark='Bogdan')
print(obj_a.print_info())
print(obj_a.name)
print(obj_a.wei)
print(obj_a.mark)

obj_b = Transport(name='Train', wei=30000, mark='Hundai')
print(obj_b.print_info())