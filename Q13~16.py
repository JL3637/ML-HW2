import numpy as np
import random

size = 128
test = 10000
r = 0.2
x_array = np.zeros(size)
y_array = np.zeros(size)
theta_array = np.zeros(size)
theta_array[0] = -0.5    #for -inf
s_array = np.array([-1,1])
E_out_minus_E_in = np.zeros(test)
for i in range(test):
    for j in range(size):
        x = random.uniform(-0.5, 0.5)
        x_array[j] = x
    x_array = np.sort(x_array)
    for j in range(size):
        rand = random.uniform(0,1)
        if rand < r:
            if x_array[j] > 0:
                y_array[j] = -1
            else:
                y_array[j] = 1
        else:
            if x_array[j] > 0:
                y_array[j] = 1
            else:
                y_array[j] = -1
    for j in range(size-1):
        theta_array[j+1] = (x_array[j] + x_array[j+1]) / 2
    opt_s = 0
    opt_theta = 0
    E_in = 1
    for j in range(2):
        wrong_data = 0
        for k in range(size):
            if y_array[k] != s_array[j]:
                wrong_data += 1
        for k in range(size):
            tmp = wrong_data / size
            if tmp < E_in:
                E_in = tmp
                opt_s = s_array[j]
                opt_theta = theta_array[k]
            if y_array[k] == s_array[j]:
                wrong_data += 1
            else:
                wrong_data -= 1
    E_out = abs(opt_theta) * (1-2*r) + r
    E_out_minus_E_in[i] = E_out - E_in

print(np.mean(E_out_minus_E_in))
    
    