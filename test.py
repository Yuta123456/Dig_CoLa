import unittest
import numpy as np
from util.calc_weight import calc_weight
from util.calc_dist import calc_dist
from util.calc_L_w import calc_l_w
from util.calc_obj import calc_obj
from util.calc_L_z import calc_l_z
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
        ans = np.array([[5/4, -1, -1/4],
                        [0, 1, -1],
                        [0, 0, 0]])
        # self.assertEqual(res, ans)
        self.check_equal_numpy_array(res, ans)

    def test_calc_dist(self):
        """
        calc_distのテスト用関数
        """
        node_cnt = 4
        edges = [[0, 1], [1, 2], [2,3], [3,1]]
        dist = calc_dist(node_cnt, edges)
        ans = np.array(([[0, 1, 2, 3],
                         [np.inf, 0, 1, 2],
                         [np.inf, 2, 0, 1],
                         [np.inf, 1, 2, 0]]))
        self.check_equal_numpy_array(dist, ans)

    def test_calc_weight(self):
        """
        calc_weightのテスト用関数
        """
        dist = np.array(([[0, 1, 2, 3],
                         [np.inf, 0, 1, 2],
                         [np.inf, 2, 0, 1],
                         [np.inf, 1, 2, 0]]))
        weight = calc_weight(dist)
        ans = 1 / dist ** 2
        self.check_equal_numpy_array(weight, ans)

    def test_calc_l_z(self):
        """
        calc_l_zのテスト用関数
        """
        node_cnt = 4
        edges = [[0, 1], [1, 2], [2,3], [3,1]]
        dist = calc_dist(node_cnt, edges)
        weight = calc_weight(dist)
        pre_x = np.array([[1,2], [2,2], [1, 4], [1,3]])
        l_pre_x = calc_l_z(node_cnt, pre_x, dist, weight)
        print(l_pre_x)
    def test_calc_obj(self):
        """
        calc_objのテスト用関数
        """
        node_cnt = 4
        edges = [[0, 1], [1, 2], [2,3], [3,1]]
        dist = calc_dist(node_cnt, edges)
        weight = calc_weight(dist)
        l_w = calc_l_w(node_cnt, weight)
        pre_x = np.array([[1,2], [2,2], [1, 4], [1,3]])
        l_pre_x = calc_l_z(node_cnt, pre_x, dist, weight)
        res = calc_obj(node_cnt, l_w, l_pre_x, pre_x[:, 0], 0)
        print(res)

    def check_equal_numpy_array(self, res, ans):
        """
        numpy行列の一致比較
        """
        self.assertEqual(res.shape, ans.shape)
        for i in zip(res.flatten(), ans.flatten()):
            self.assertEqual(i[0], i[1])
if __name__ == "__main__":
    unittest.main()
