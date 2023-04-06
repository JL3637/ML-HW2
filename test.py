import numpy as np
import random

filename_1 = 'data.txt'

s_array = np.array([-1, 1])

train_size = 192
train_array = np.ones([train_size, 11])
with open(filename_1) as file:
    a = 0
    for line in file:
        line = line.strip().split()
        for i in range(11):
            train_array[a][i] = line[i]
        a += 1
file.close()

i = 9
E_in = 1
opt_theta = 0
opt_s = 0
train_array = train_array[train_array[:, i].argsort()]
wrong_data = 0
for k in range(train_size):
    if train_array[k][10] != s_array[0]:
        wrong_data += 1
for k in range(train_size-1):
    tmp = wrong_data / train_size
    if tmp < E_in:
        E_in = tmp
        opt_theta = k
        opt_s = -1
    if train_array[k][10] == s_array[0]:
        wrong_data += 1
    else:
        wrong_data -= 1
wrong_data = 0
for k in range(train_size):
    if train_array[k][10] != s_array[1]:
        wrong_data += 1
for k in range(train_size):
    tmp = wrong_data / train_size
    if tmp < E_in:
        E_in = tmp
        opt_theta = k
        opt_s = 1
    if train_array[k][10] == s_array[1]:
        wrong_data += 1
    else:
        wrong_data -= 1

print(E_in)
print((train_array[opt_theta-1][i] + train_array[opt_theta][i]) / 2, opt_s)