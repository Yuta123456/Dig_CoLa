from scipy.sparse.csgraph import shortest_path
import sys
import numpy as np

def calc_weight(n, W, alpha=-2):
    """
    L^wを求める。グラフ構造から導出される重み係数行列である。

    Parameters
    ----------
    n : int
        ノード数
    W : np.ndarray
        グラフの重み行列
    alpha : int
        重みのパラメタ
    Returns
    -------
    L_w : np.ndarray
        対象グラフの重み係数行列
    """
    L_w = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                # もし、i != jであれば、- W[i][j]
                L_w[i][j] = - W[i][j]
            else:
                # そうでなければ、d_{ik}^\alpha (k != i)の合計
                L_w[i][j] = sum([W[i][j] if k != i else 0 for k in range(n)])
    return L_w
