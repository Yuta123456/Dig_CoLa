import sys
import numpy as np
from scipy.sparse.csgraph import shortest_path

def calc_dist(n, edges):
    """
    グラフの最短経路を計算。

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
    # ノードの接続情報から隣接行列を作成
    adjusent_list = [[0 for j in range(n)] for i in range(n)]
    for e in edges:
        src = e[0]
        tar = e[1]
        try: 
            weight = e[2]
        except IndexError:
            # 重みが設定されていない場合には、重みなし辺と認識し、1を設定
            weight = 1
        except Exception as e:
            print(e)
            sys.exit(1)

        adjusent_list[src][tar] = weight
    dist = shortest_path(np.array(adjusent_list))
    return dist