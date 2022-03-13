from scipy.sparse.csgraph import shortest_path
import sys
import numpy as np
def calc_L_z(n, Z, dist,  W, alpha=-2):
    """
    L^zを求める。X^tからX^{t+1}を導出するのに必要な行列である。

    Parameters
    ----------
    n : int
        ノード数
    Z : np.ndarray
        1step前の座標ベクトル
    dist : np.ndarray
        グラフの距離行列
    W : np.ndarray
        重み係数行列である。
    alpha : int
        重みのパラメタ
    Returns
    -------
    L^z : np.ndarray
        対象グラフの重み係数行列
    """
    
    L_z = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                sub = (Z[i] - Z[j]) ** 2
                sub_sum = sum(sub)
                if sub_sum == 0:
                    sub_inv = 0
                else:
                    sub_inv = 1 / sum(sub)
                L_z[i][j] = -W[i][j] * dist[i][j] * sub_inv
    
    for i in range(n):
        L_z[i][i] = - sum([L_z[i][j] if j != i else 0 for j in range(n)])
    
    return L_z