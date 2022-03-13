import numpy as np

def calc_weight(dist, alpha=-2):
    """
    Wを求める。重み係数行列である。

    Parameters
    ----------
    dist : np.ndarray
        グラフの最短距離行列
    alpha : int
        重みのパラメタ
    Returns
    -------
    W : np.ndarray
        対象グラフの重み係数行列
    """
    W = np.empty(dist.shape)
    for i in range(dist.shape[0]):
        for j in range(dist.shape[1]):
            # TODO: dist[i][j] = 0の時コケるかも
            W[i][j] = pow(dist[i][j], alpha)
    return W
