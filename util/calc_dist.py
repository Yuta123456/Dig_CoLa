import numpy as np
from scipy.sparse.csgraph import shortest_path

class InfError(Exception):
    """
    距離がinfになった際、グラフが連結でないことがわかる。
    """
    def __str__(self):
        return "グラフが連結じゃありません"
def calc_dist(node_cnt, edges):
    """
    グラフの最短経路を計算。
    NOTE : 有効グラフが与えられた際も、無向グラフとして計算している。
    Parameters
    ----------
    node_cnt : int
        ノード数
    edges : np.ndarray
        辺の接続情報
    Returns
    -------
    L_w : np.ndarray
        対象グラフの重み係数行列
    """
    # ノードの接続情報から隣接行列を作成
    adjusent_list = [[0 for j in range(node_cnt)] for i in range(node_cnt)]
    for edge in edges:
        src = edge[0]
        tar = edge[1]
        try: 
            weight = edge[2]
        except IndexError:
            # 重みが設定されていない場合には、重みなし辺と認識し、1を設定
            weight = 1

        adjusent_list[src][tar] = weight
        adjusent_list[tar][src] = weight
    dist = shortest_path(np.array(adjusent_list))
    if not np.all(dist != np.inf):
        raise InfError()
    return dist
