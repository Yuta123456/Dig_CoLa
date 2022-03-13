import unittest
from util.calc_weight import calc_weight 
import numpy as np

class Test(unittest.TestCase):
    def test_calc_weight(self):
        edges = [[0,1], [1,2]]
        res = calc_weight(3, edges)
        ans = np.array([[5/4, -1, -1/4], [0, 1, -1], [0, 0, 0]])
        # self.assertEqual(res, ans)
        self.assertEqual(res.shape, ans.shape)
        for i in zip(res.flatten(), ans.flatten()):
            self.assertEqual(i[0], i[1])

if __name__ == "__main__":
    unittest.main()
