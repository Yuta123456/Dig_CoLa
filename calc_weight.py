
def calc_weight(n, edges):
    """
    L^wを求める。グラフ構造から導出される重み係数行列である。

    Parameters
    ----------
    n : int
        ノード数
    edges : np.ndarray
        辺の接続情報 

    Returns
    -------
    L_w : np.ndarray
        対象グラフの重み係数行列
    """
