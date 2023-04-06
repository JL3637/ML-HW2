import numpy as np
import random

filename_1 = 'data.txt'
filename_2 = 'data-test.txt'

inf = 1000000
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

test_size = 64
test_array = np.ones([test_size, 11])
with open(filename_2) as file:
    a = 0
    for line in file:
        line = line.strip().split()
        for i in range(11):
            test_array[a][i] = line[i]
        a += 1
file.close()

opt_s = 0
opt_theta = 0
opt_i = 0
E_in = 1
opt_s_wob = 0
opt_theta_wob = 0
opt_i_wob = 0
E_in_wob = 0
theta_array = np.zeros(train_size)
theta_array[0] = -inf
for i in range(10):
    tmp_wob = 1
    opt_s_wob_2 = 0
    opt_theta_wob_2 = 0
    opt_i_wob_2 = 0
    train_array = train_array[train_array[:, i].argsort()]
    for j in range(train_size-1):
        theta_array[j+1] = (train_array[j][i] + train_array[j+1][i]) / 2
    for j in range(2):
        wrong_data = 0
        for k in range(train_size):
            if train_array[k][10] != s_array[j]:
                wrong_data += 1
        for k in range(train_size):
            tmp = wrong_data / train_size
            tmp_wob_2 = wrong_data / train_size
            if tmp < E_in:
                E_in = tmp
                opt_theta = theta_array[k]
                opt_s = s_array[j]
                opt_i = i
            if tmp_wob_2 < tmp_wob:
                tmp_wob = tmp_wob_2
                opt_theta_wob_2 = theta_array[k]
                opt_s_wob_2 = s_array[j]
                opt_i_wob_2 = i
            if train_array[k][10] == s_array[j]:
                wrong_data += 1
            else:
                wrong_data -= 1
    if tmp_wob > E_in_wob:
        E_in_wob = tmp_wob
        opt_i_wob = opt_i_wob_2
        opt_s_wob = opt_s_wob_2
        opt_theta_wob = opt_theta_wob_2
print(E_in)
print(E_in_wob)
print(E_in_wob - E_in)
print(opt_i, opt_s, opt_theta)
print(opt_i_wob, opt_s_wob, opt_theta_wob)

test_array = test_array[test_array[:, opt_i].argsort()]
wrong_data = 0
wrong_data_wob = 0
for i in range(test_size):
    if (opt_s * (test_array[i][opt_i] - opt_theta) > 0 and test_array[i][10] == -1) or (opt_s * (test_array[i][opt_i] - opt_theta) <= 0 and test_array[i][10] == 1):
        wrong_data += 1
    if (opt_s_wob * (test_array[i][opt_i_wob] - opt_theta_wob) > 0 and test_array[i][10] == -1) or (opt_s_wob * (test_array[i][opt_i_wob] - opt_theta_wob) <= 0 and test_array[i][10] == 1):
        wrong_data_wob += 1
E_out = wrong_data / test_size
E_out_wob = wrong_data_wob / test_size
print(E_out)
print(E_out_wob)
print(E_out_wob - E_out)