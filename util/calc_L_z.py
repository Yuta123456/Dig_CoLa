import sys
import numpy as np
def calc_l_z(node_cnt, z_array, dist, weight):
    """
    L^zを求める。X^tからX^{t+1}を導出するのに必要な行列である。

    Parameters
    ----------
    node_cnt : int
        ノード数
    z_array : np.ndarray
        1step前の座標ベクトル
    dist : np.ndarray
        グラフの距離行列
    weight : np.ndarray
        重み係数行列。
    alpha : int
        重みのパラメタ
    Returns
    -------
    L^z : np.ndarray
        対象グラフの重み係数行列
    """

    l_z = np.empty((node_cnt, node_cnt))
    for i in range(node_cnt):
        for j in range(node_cnt):
            if i != j:
                sub = (z_array[i] - z_array[j]) ** 2
                sub_sum = sum(sub)
                if sub_sum == 0:
                    sub_inv = 0
                else:
                    sub_inv = 1 / sum(sub)
                l_z[i][j] = -weight[i][j] * dist[i][j] * sub_inv
                # FIXME: 0 * np.inf = nanになってしまい、困ってる
                print(f"\n\nl_z[i][j]:{l_z[i][j]}, -weight[i][j]: {weight[i][j]}, dist[i][j]:{dist[i][j]}, sub_inv: {sub_inv}")

    for i in range(node_cnt):
        l_z[i][i] = - sum([l_z[i][j] if j != i else 0 for j in range(node_cnt)])

    return l_z
