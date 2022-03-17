import unittest
import numpy as np
from util.calc_weight import calc_weight
from util.calc_dist import calc_dist
from util.calc_L_w import calc_l_w
class Test(unittest.TestCase):
    """
    テスト用クラス
    """
    def test_calc_l_w(self):
        """
        calc_L_w関数のテスト用関数
        """
        node_cnt = 3
        edges = [[0,1], [1,2]]
        dist = calc_dist(node_cnt, edges)
        weight = calc_weight(dist)
        res = calc_l_w(node_cnt, weight)
        ans = np.array([[5/4, -1, -1/4], [0, 1, -1], [0, 0, 0]])
        # self.assertEqual(res, ans)
        self.assertEqual(res.shape, ans.shape)
        for i in zip(res.flatten(), ans.flatten()):
            self.assertEqual(i[0], i[1])

if __name__ == "__main__":
    unittest.main()
