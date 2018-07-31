import numpy as np

array_2d = np.arange(1,26,1).reshape(5,5)

print(array_2d, '\n')

print(array_2d[2:,1:], '\n')

print(array_2d[3,4], '\n')

print(array_2d[0:3,1].reshape(3,1), '\n')

print(np.sum(array_2d,axis=0))