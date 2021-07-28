# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:12:17 2021

@author: zongsing.huang
"""

import numpy as np
import matplotlib.pyplot as plt

def fit_func(X):
    x = X[0]
    y = X[1]
    score = (x**2 + y - 11)**2 + (x + y**2 - 7)**2
    
    return score

T0 = 1000
max_M = 300
max_N = 15
alpha = 0.85
k = 0.1
ub = 6
lb = -6

loss = np.zeros(max_M)
x = np.random.uniform(low=lb, high=ub, size=2)

for m in range(max_M):
    for n in range(max_N):
        
        # 更新
        delta_x = np.zeros(2)
        
        r1 = np.random.uniform()
        r2 = np.random.uniform()
        if r1>=0.5:
            delta_x[0] = k*r2
        else:
            delta_x[0] = -k*r2
        
        r3 = np.random.uniform()
        r4 = np.random.uniform()
        if r3>=0.5:
            delta_x[1] = k*r4
        else:
            delta_x[1] = -k*r4
        
        new_x = x + delta_x
        
        # 邊界處理
        mask1 = new_x>ub
        mask2 = new_x<lb
        new_x[mask1] = ub
        new_x[mask2] = lb
        
        # 適應值計算
        new_fitness = fit_func(new_x)
        fitness = fit_func(x)
        
        # 取代
        r5 = np.random.uniform()
        formula = np.exp((fitness - new_fitness)/T0) # 越小越好
        # formula = np.exp(-1*(fitness - new_fitness)/T0) # 越大越好
        if new_fitness<fitness or r5<formula:
            x = new_x.copy()
        else:
            pass
    
    loss[m] = fitness.copy()
    T0 = alpha*T0
            
plt.figure()
plt.plot(loss)
plt.grid()
        