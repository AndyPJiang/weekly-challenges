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

    def test_example_1_binary_tree(self):
        root = TreeNode(1)
        root.children.append(TreeNode(2)) 
        root.children.append(TreeNode(3))
        root.children[0].children.append(TreeNode(4)) 
        test_tree = Tree(root)
        self.assertEqual(test_tree.longest_path_in_tree(), 2)

    def test_example_2_binary_tree(self):
        root = TreeNode(5)
        root.children.append(TreeNode(12))
        root.children.append(TreeNode(7))
        root.children[1].children.append(TreeNode(8))
        root.children[1].children.append(TreeNode(6))
        root.children[1].children[0].children.append(TreeNode(9))
        root.children[1].children[0].children[0].children.append(TreeNode(15))
        root.children[1].children[0].children[0].children.append(TreeNode(10))
        test_tree = Tree(root)
        self.assertEqual(test_tree.longest_path_in_tree(), 4)

    def test_stick_tree_binary_tree(self):
        root = TreeNode(5)
        root.children.append(TreeNode(10))
        root.children[0].children.append(TreeNode(11))
        root.children[0].children[0].children.append(TreeNode(13))
        root.children[0].children[0].children[0].children.append(TreeNode(14))
        root.children[0].children[0].children[0].children[0].children.append(TreeNode(15))

        test_tree = Tree(root)
        self.assertEqual(test_tree.longest_path_in_tree(), 3)

    def test_example_3_nary_tree(self):
        root = TreeNode(5)
        root.children.append(TreeNode(1))
        root.children.append(TreeNode(2))
        root.children.append(TreeNode(3))
        root.children.append(TreeNode(4))
        root.children[0].children.append(TreeNode(20))
        root.children[0].children.append(TreeNode(6))
        root.children[0].children.append(TreeNode(14))
        root.children[1].children.append(TreeNode(18))
        root.children[1].children.append(TreeNode(19))
        root.children[1].children.append(TreeNode(100))
        root.children[2].children.append(TreeNode(7))
        root.children[2].children.append(TreeNode(200))
        root.children[2].children[0].children.append(TreeNode(8))
        root.children[2].children[0].children[0].children.append(TreeNode(9))
        root.children[2].children[0].children[0].children[0].children.append(TreeNode(10))
        test_tree = Tree(root)
        self.assertEqual(test_tree.longest_path_in_tree(), 4)

if __name__ == "__main__":
  unittest.main()