import numpy as np
import sympy

def calc_obj(node_cnt, l_w, l_pre_x, pre_x_at_a):
    """
    特定の次元の目的関数を計算

    Parameters
    ----------
    node_cnt : np.ndarray
        ノード数
    L^w : np.ndarray
        グラフ構造から導出される重み係数行列。
    L^pre_x : np.ndarray
        X(t-1)から導出される行列
    pre_x_at_a : np.ndarray
        X(t-1), つまり、前のノードの位置。そのa次元のみ抽出したベクトル
    Returns
    -------
        TODO: 最適化したい数式
    """
    x = np.array([])
    for i in range(1, node_cnt+1):
        x = np.append(x, sympy.Symbol(f"x_{i}"))
    obj = np.dot(np.dot(x.T, l_w), x)
    obj_2 = 2 * np.dot(np.dot(x, l_pre_x), pre_x_at_a)
    obj = obj - obj_2
    obj = sympy.expand(obj)
    return obj
