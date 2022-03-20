
from util.determine_node_point import determine_node_point
from util.calc_stress_x import calc_stress_x
from util.calc_dist import calc_dist
from util.calc_weight import calc_weight
import numpy as np
node_cnt = 5
edges = [[0,3], [1,2], [2,3], [0,4]]
initial_points = np.array([[np.random.randint(10000),np.random.randint(10000)] for i in range(node_cnt)])
initial_points[-1] = np.array([0, 0])
dimension = 2
points = determine_node_point(node_cnt, edges, initial_points, dimension)
print(points)
