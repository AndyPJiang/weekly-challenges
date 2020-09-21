# week3
class TreeNode:
    def __init__(self, data: int, left=None, right=None):
        self.right = left
        self.left = right
        self.data = data


class Tree:
    def __init__(self, root: TreeNode):
        self.root = root

    def longest_path_in_tree(self) -> int:
        if not self.root:
            return 0
        return self.longest_path_recur(self.root, 1)
    
    def longest_path_recur(self,root,longest) -> int:
        longest_right = longest
        longest_left = longest

        if root.right:
            if root.right.data == root.data+1:
                longest_right = max(longest_right, self.longest_path_recur(root.right, longest+1))
            longest_right = max(longest_right, self.longest_path_recur(root.right, 1))

        if root.left:
            if root.left.data == root.data+1:
                longest_left = max(longest_left, self.longest_path_recur(root.left, longest+1))
            longest_left = max(longest_left, self.longest_path_recur(root.left, 1))

        return max(longest_right,longest_left)





