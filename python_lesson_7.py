
import numpy as np

a = np.array([-1,1,2,3,4,5,6,7], dtype=float)
a_list = [1,2,3,4,5,6,7]
print((a + 3) * 2, a - 1)
print(f'Max of a: {a.max()}\nMin of a:{a.min()}')
print(a.max(), a.min(), a.mean(), a.sum(), a.std())

x_2d = np.array([
    [12,24,36],
    [4,5,6]
])
print(x_2d[0][2], x_2d[0].min(), x_2d[1].min())


x = np.array([[[i + j + k for k in range(5)] for j in range(4)] for i in range(3)])
print(x_2d.shape)
print(x.shape)
print(x.size, x_2d.size)

one_matrix = np.ones((4, 1), dtype=np.float)
print(one_matrix, one_matrix.size, one_matrix.shape)
print(x_2d[0].sum(), x_2d[1].sum(), len(x_2d[0]), x_2d[0].size)
print('Second part of lesson')
print(x_2d)
print(x_2d[1::])