import unittest
from week4 import LargestSumRectangle


class Longest_path_in_tree(unittest.TestCase):
    def test_empty_grid(self):
        grid = []
        inst = LargestSumRectangle(grid)
        self.assertEqual(inst.findLargestRectangle(), ())

    def test_example1(self):
        grid = [[1,2],[3,4,5,6],[7,8],[9]]
        inst = LargestSumRectangle(grid)
        self.assertEqual(inst.findLargestRectangle(), ((0,0),(2,1)))

    def test_example2(self):
        grid = [[1,3,2,2],[2,1,2,3],[4,2,3],[1,1,2,17,14],[3,1,2,2]]
        inst = LargestSumRectangle(grid)
        self.assertEqual(inst.findLargestRectangle(), ((3,0),(3,4)))
    def test_1d_grid(self):
        grid = [[14,3,2]]
        inst = LargestSumRectangle(grid)
        self.assertEqual(inst.findLargestRectangle(), ((0,0),(0,2)))
    def test_with_empty_row(self):
        grid = [[101,12,12,1],[],[3,2,2,3,4,2],[41,12,3]]
        inst = LargestSumRectangle(grid)
        self.assertEqual(inst.findLargestRectangle(), ((0,0),(0,3)))
    def test_others1(self):
        grid = [[1,2,2,2,3],[1,2,3,4,5,6],[10000]]
        inst = LargestSumRectangle(grid)
        self.assertEqual(inst.findLargestRectangle(), ((0,0),(2,0)))
if __name__ == "__main__":
  unittest.main()