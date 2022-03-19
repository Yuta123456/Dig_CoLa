import numpy as np
import sympy
def calc_q_o(node_cnt, exp):
    """
    最適化の際に必要なQ_oを導出する関数。
    (1/2) * (X^T)Q_oXが最小化したい式になるようなQを計算。

    Parameters
    ----------
    node_cnt : int
        ノードの個数
    f_x : sympy.core.add.Add
        最小化したい数式

    Returns
    -------
    q_o : np.ndarray
        係数行列。
    """
    q_o = np.empty((node_cnt, node_cnt))
    for i in range(node_cnt):
        for j in range(node_cnt):
            a = i+1
            b = j+1
            x = sympy.Symbol(f'x_{a}')
            y = sympy.Symbol(f'x_{b}')
            q_o[i][j] = exp.coeff(x*y, 1)
            if i == j:
                q_o[i][j] *= 2
    return q_o
