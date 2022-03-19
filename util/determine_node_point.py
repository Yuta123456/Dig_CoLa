import numpy as np
from util.calc_L_w import calc_l_w
from util.calc_weight import calc_weight
from util.calc_dist import calc_dist
from util.calc_stress_x import calc_stress_x
from util.calc_obj import calc_obj
from util.calc_L_z import calc_l_z
from util.calc_node_point import calc_node_point
def determine_node_point(node_cnt, edges, initial_points, dimension, eps=0.01):
    """
    ノードの描画位置を決める関数
    """
    delta = eps + 1
    dist = calc_dist(node_cnt, edges)
    weight = calc_weight(dist)
    l_w = calc_l_w(node_cnt, weight)
    pre_points = initial_points
    stress_x = calc_stress_x(node_cnt, weight, dist, initial_points)
    # 差分がepsより多い間続ける
    while delta > eps:
        new_points = np.empty((node_cnt, dimension))
        l_pre_x = calc_l_z(node_cnt, initial_points, dist, weight)
        for axis in range(dimension):
            # if axis == 1:
                # TODO: y軸に対しては制約を課す
            exp = calc_obj(node_cnt, l_w, l_pre_x, pre_points[:, axis])
            # axisに対しての最適解が返ってくるため、1 * nのベクトル
            point = calc_node_point(node_cnt, exp)
            new_points[:, axis] = point.T
        pre_points = new_points
        new_stress_x = calc_stress_x(node_cnt, weight, dist, new_points)
        delta = (stress_x - new_stress_x) / stress_x
        stress_x = new_stress_x
    return new_points
