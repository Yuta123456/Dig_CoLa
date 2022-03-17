import numpy as np

def calc_l_w(node_cnt, weight):
    """
    L^wを求める。グラフ構造から導出される重み係数行列である。

    Parameters
    ----------
    node_cnt : int
        ノード数
    weight : np.ndarray
        グラフの重み行列
    Returns
    -------
    L_w : np.ndarray
        対象グラフの重み係数行列
    """
    l_w = np.empty((node_cnt, node_cnt))
    for i in range(node_cnt):
        for j in range(node_cnt):
            if i != j:
                # もし、i != jであれば、- W[i][j]
                l_w[i][j] = - weight[i][j]
            else:
                # そうでなければ、d_{ik}^\alpha (k != i)の合計
                l_w[i][j] = sum([weight[i][j] if k != i else 0 for k in range(node_cnt)])
    return l_w
