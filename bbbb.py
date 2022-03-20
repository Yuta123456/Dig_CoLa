import numpy as np
import sympy

from util.calc_weight import calc_weight
from util.calc_dist import calc_dist
from util.calc_L_w import calc_l_w

node_cnt = 5
edges = [[1,2], [0,2], [3,4], [2,4]]
dist = calc_dist(node_cnt, edges)
w = calc_weight(dist)
l_w = np.zeros((node_cnt, node_cnt));
for j in range(1,node_cnt-1):
    for i in range(j):
        wij = w[i][j]
        l_w[i-1][j] = -wij
        l_w[j-1][i] = -wij
        l_w[i-1][i] += wij
        l_w[j-1][j] += wij
    
for i in range(node_cnt- 1):
    j = node_cnt - 1
    l_w[i-1][i] += w[i][j]
print(l_w)

old_l_w = calc_l_w(node_cnt, w)
print(old_l_w)