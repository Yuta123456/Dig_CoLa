import unittest
import numpy as np
import sympy
from util.calc_q_o import calc_q_o
from util.calc_c import calc_c
class Test(unittest.TestCase):
    """
    テスト用クラス
    """
    def test_calc_q_o(self):
        """
        calc_q_oのテスト関数
        """
        node_cnt = 10
        x = np.array([], dtype=np.int64)
        for i in range(1, node_cnt+1):
            x = np.append(x, sympy.Symbol(f'x_{i}'))
        ans = np.empty((node_cnt, node_cnt), dtype=np.int64)
        for i in range(node_cnt):
            for j in range(i, node_cnt):
                ans[i][j] = np.random.randint(1,20)
                ans[j][i] = ans[i][j]
        
        exp = (1/2) * np.dot(np.dot(x, ans), x.T)
        res = calc_q_o(node_cnt, sympy.expand(exp))
        self.check_equal_numpy_array(res, ans)

    def test_calc_c(self):
        """
        calc_cのテスト用関数
        """
        node_cnt = 3
        x = np.array([], dtype=np.int64)
        for i in range(1, node_cnt+1):
            x = np.append(x, sympy.Symbol(f'x_{i}'))
        exp = x[0] * 3 + x[1] * 8 + x[2] * 2 + x[0] * x[1] * 12 + 5 * x[1]**2 * x[2] 
        exp = sympy.expand(exp)
        res = calc_c(node_cnt, exp)
        ans = np.array([3, 8, 2])
        self.check_equal_numpy_array(res, ans)
        
    def check_equal_numpy_array(self, res, ans):
        """
        numpy行列の一致比較
        """
        self.assertEqual(res.shape, ans.shape)
        for i in zip(res.flatten(), ans.flatten()):
            self.assertEqual(i[0], i[1])

if __name__ == "__main__":
    unittest.main()