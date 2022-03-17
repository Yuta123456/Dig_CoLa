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
    # TODO: distの中に0が入っていた場合、
    #       RuntimeWarning: divide by zero encountered in true_divideが起こる
    weight = dist ** alpha
    return weight
