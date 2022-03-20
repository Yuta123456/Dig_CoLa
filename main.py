
from util.determine_node_point import determine_node_point
from util.calc_stress_x import calc_stress_x
from util.calc_dist import calc_dist
from util.calc_weight import calc_weight
import networkx as nx
import numpy as np
node_cnt = 8
graph = nx.binomial_tree(3)
edges = list(graph.edges())
initial_points = np.array([[np.random.randint(1000,10000),np.random.randint(1000,10000)] for i in range(node_cnt)])
initial_points[-1] = np.array([0, 0])
dimension = 2
points = determine_node_point(node_cnt, edges, initial_points, dimension)
print(points)

pos = {u: (xi, yi) for u, xi, yi in zip(graph.nodes(), points[:, 0], points[:, 1])}
nx.draw(graph, pos)