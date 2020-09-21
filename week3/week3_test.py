import unittest
from week3 import Tree, TreeNode


class Longest_path_in_tree(unittest.TestCase):
    def test_empty_tree(self):
        root = None
        test_tree = Tree(root)
        self.assertEqual(test_tree.longest_path_in_tree(), 0)

    def test_one_node(self):
        root = TreeNode(100)
        test_tree = Tree(root)
        self.assertEqual(test_tree.longest_path_in_tree(), 1)

    def test_example_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        test_tree = Tree(root)
        self.assertEqual(test_tree.longest_path_in_tree(), 2)

    def test_example_2(self):
        root = TreeNode(5)
        root.left = TreeNode(12)
        root.right = TreeNode(7)
        root.right.right = TreeNode(6)
        root.right.left = TreeNode(8)
        root.right.left.left = TreeNode(9)
        root.right.left.left.left = TreeNode(15)
        root.right.left.left.right = TreeNode(10)
        test_tree = Tree(root)
        self.assertEqual(test_tree.longest_path_in_tree(), 4)

    def test_stick_tree(self):
        root = TreeNode(5)
        root.right = TreeNode(10)
        root.right.right = TreeNode(11)
        root.right.right.right = TreeNode(12)
        root.right.right.right.right = TreeNode(14)
        root.right.right.right.right.right = TreeNode(15)
        root.right.right.right.right.right.right = TreeNode(16)
        root.right.right.right.right.right.right.right = TreeNode(17)
        root.right.right.right.right.right.right.right.right = TreeNode(18)

        test_tree = Tree(root)
        self.assertEqual(test_tree.longest_path_in_tree(), 5)

    
test = Longest_path_in_tree()
test.test_empty_tree()
test.test_one_node()
test.test_example_1()
test.test_example_2()
test.test_stick_tree()
