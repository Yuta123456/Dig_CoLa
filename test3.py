import unittest
import sympy
from util.calc_node_point import calc_node_point
class Test(unittest.TestCase):
    """
    テスト用クラス
    """
    def test_calc_node_point(self):
        """
        ノードの座標を取得
        """
        node_cnt = 3
        x1 = sympy.Symbol('x_1')
        x2 = sympy.Symbol('x_2')
        x3 = sympy.Symbol('x_3')
        exp = x1**2 + 0.1*x2**2 + x3**2 - x1*x3 - x2
        optional_solution = calc_node_point(node_cnt, exp)


if __name__ == "__main__":
    unittest.main()