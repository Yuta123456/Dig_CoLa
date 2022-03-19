import numpy as np
import sympy
def calc_c(node_cnt, exp):
    """
    最適化の際に必要なcを導出する関数。
    実際は最小化したい式の変数、1次のものの係数を並べたもの
    Parameters
    ----------
    node_cnt : int
        ノード数
    exp : sympy.core.add.Add
        最小化したい式

    Returns
    -------
    c : np.ndarray
        一次の係数ベクトル
    """
    c = np.empty((node_cnt, ))
    for i in range(node_cnt):
        x = sympy.Symbol("x_{}".format(i+1))
        # その式のxの係数を取得
        exp_x = exp.coeff(x, 1)
        # その後、全ての他の変数に0を代入する。
        # TODO: もっといい方法ありそう。
        for j in range(node_cnt):
            if i != j:
                y = sympy.Symbol("x_{}".format(j+1))
                exp_x = exp_x.subs([(y, 0)])
        c[i] = exp_x
    return c
