from scipy.sparse.csgraph import shortest_path
import sys
import numpy as np
def calc_weight(n, edges, alpha=-2):
    """
    L^wを求める。グラフ構造から導出される重み係数行列である。

    Parameters
    ----------
    n : int
        ノード数
    edges : np.ndarray
        辺の接続情報 
    alpha : int
        重みのパラメタ
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
    L_w = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                # もし、i != jであれば、-d_{ij}^\alpha
                L_w[i][j] = - pow(dist[i][j], alpha)
            else:
                # そうでなければ、d_{ik}^\alpha (k != i)の合計
                L_w[i][j] = sum([pow(dist[i][k], alpha) if k != i else 0 for k in range(n)])
    return L_w
