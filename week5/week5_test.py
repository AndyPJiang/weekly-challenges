import unittest
from week5 import LongestWordInGrid


class Longest_path_in_tree(unittest.TestCase):
    def test_empty_grid(self):
        grid = []
        inst = LongestWordInGrid(grid)
        self.assertEqual(inst.longestWord(), "")
    
    def test_example_1(self):
        grid = [
            ["F","X","I","E"],
            ["A","M","X","O"],
            ["E","W","B","C"],
            ["A","S","T","U"]
        ]
        inst = LongestWordInGrid(grid)
        self.assertEqual(inst.longestWord(), "FAMES")

    def test_example2(self):
        grid = [
            ["F","X","E","I"],
            ["A","M","L","O"],
            ["E","W","B","X"],
            ["A","S","T","U"]
        ]
        inst = LongestWordInGrid(grid)
        self.assertEqual(inst.longestWord(), "EMBOIL")

    def test_1d_grid(self):
        grid = [
            ["H","E","L","L","O","W"],
        ]
        inst = LongestWordInGrid(grid)
        self.assertEqual(inst.longestWord(), "HELLO")
    
    def test_diagonal_word(self):
        grid = [
            ["H","E","L","W"],
            ["H","E","L","W"],
            ["H","E","L","W"],
            ["H","E","M","L"],
        ]
        inst = LongestWordInGrid(grid)
        self.assertEqual(inst.longestWord(), "HELL")


    def test_diagonal_word(self):
        grid = [
            ["H","E","L","W"],
            ["H","E","L","W"],
            ["H","E","L","W"],
            ["H","E","M","L"],
        ]
        inst = LongestWordInGrid(grid)
        self.assertEqual(inst.longestWord(), "HELL")
    
    def test_no_words(self):
        grid = [
            ["H","E","L","W"],
            ["H","E","Q","W"],
            ["H","E","L","W"],
            ["H","E","M","S"],
        ]
        inst = LongestWordInGrid(grid)
        self.assertEqual(inst.longestWord(), "")

if __name__ == "__main__":
  unittest.main()