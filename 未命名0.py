# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 22:58:00 2021

@author: ZongSing_NB2
"""

import numpy as np

y = np.array([0.5, 14.0, 15.0, 28.0, 11.0, 8.0, 3.0, -4.0, 6.0, 13.0, 21.0])
x = np.array([35.7, 55.9, 58.2, 81.9, 56.3, 48.9, 33.9, 21.8, 48.4, 60.4, 68.4])

# 初始化
w, b = 1.0, 0.0
G = 100
lr = 1e-4

for g in range(G):
    
    # 預測
    pred_y = w*x + b
    
    # 誤差
    loss = ( (pred_y-y)**2 ).mean()
    print('Iteration {g:.2f}, loss {loss:.2f}, w is {w:.2f}, b is {b:.2f}'.format(g=g, loss=loss, w=w, b=b))
    
    # 變化量
    delta_w = ( 2 * (pred_y-y) * x ).mean()
    delta_b = ( 2 * (pred_y-y) ).mean()
    
    # 更新
    w = w - lr*delta_w
    b = b - lr*delta_b