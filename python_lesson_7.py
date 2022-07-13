
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
lins = np.linspace(0, 1, 20)
print(lins)
print(a[-1])

x_2 = np.array([[i for i in range(10, 20)], [i for i in range(100, 110)]])

print(x_2)
print(x_2.shape, x_2.size, x_2[0, 4] == x_2[0][4])
print(x_2[:, 4:6], x_2[1, 0:2] == x_2[1][0:2])
print(x_2[::-1, :]) # add x_2[::-1][:]

some_np = np.array([
    ['a', 'b','c'],
    ['d', 'e', 'f']
                   ])

print(some_np[0,0:2], ord('a'), chr(97))

vector = np.arange(12)
print(vector.shape, vector.size, vector.min(), vector.max())
print(vector.reshape((3,-3)))
print(vector.reshape(2,6))
# inf

print(np.sqrt(vector), np.sin(vector))
#print(np.log2(vector))
print(vector.astype(np.float_))

print(f'Mediana of vector {np.median(vector)}, Med: {vector.mean()}')

x_ones = np.ones((1, 2, 3))
print(x_ones.size, x_ones.shape)
print(x_ones.sum(axis=2))
print([1,2,3 ] + [4,5,6])

x_req = [1,2,3,4]

r = x_req.copy()
print(x_req)
x_req.append(6)

print(r, x_req)