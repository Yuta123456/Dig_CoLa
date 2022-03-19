def calc_stress_x(node_cnt, weight, dist, node_points):
    """
    ストレス関数を計算
    """
    stress_score = 0
    for i in range(node_cnt):
        for j in range(i+1, node_cnt):
                # TODO: あってる気がしない。確認
                stress_score += weight[i][j] * (sum((node_points[i] - node_points[j]) ** 2) - dist[i][j]) ** 2

    return stress_score