import numpy as np
import sympy

def calc_obj(node_cnt, l_w, l_pre_x, pre_x_at_a, axis):
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
    axis : int
        次元
    Returns
    -------
        TODO: なんか書く
    """
    x = np.array([])
    for i in range(node_cnt):
        x = np.append(x, sympy.Symbol(f"x_{axis}{i}"))
    obj = np.dot(np.dot(x.T, l_w), x)
    print(f"\n\nx.T: {x.T.shape}, l_pre_x: {l_pre_x.shape}, pre_x_at_a: {pre_x_at_a.shape}")
    print(f"\n\n{l_pre_x}\n\n")
    obj_2 = 2 * np.dot(np.dot(x, l_pre_x), pre_x_at_a)
    print(sympy.expand(obj), obj_2)
    return obj - obj_2
