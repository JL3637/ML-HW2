import numpy as np
import random

size = 2
data_set = np.zeros(size)
E_out_minus_E_in = np.zeros(10000)
for j in range(size):
    x = random.uniform(-0.5, 0.5)
    data_set[j] = x
a = np.array([5,4,3,2,1])
print(data_set)
data_set = np.sort(data_set)
print(data_set)
wrong_data = 0
for j in range(size):
    if data_set[j] > 0:
        wrong_data = j
E_in = wrong_data / size
for j in range(size):
    if data_set[j] > 0:
        wrong_data += 1
    else:
        wrong_data -= 1
    tmp = wrong_data / size
    if tmp < E_in:
        E_in = tmp