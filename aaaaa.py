import numpy as np
import sympy

from util.calc_weight import calc_weight
from util.calc_dist import calc_dist
from util.calc_L_w import calc_l_w
node_cnt = 4
edge = [[0,1], [2,3], [0,3], [1,2]]
dist = calc_dist(node_cnt, edge)
weight = calc_weight(dist)
x = np.array([[1, 2], [2, 5],[3, 2], [5, 3]])
l_w = calc_l_w(node_cnt, weight)
print(np.dot(np.dot(x.T, l_w), x))