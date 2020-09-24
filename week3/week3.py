# week3
class TreeNode:
    def __init__(self, data: int, children=[]):
        self.children = []
        self.data = data

class Tree:
    def __init__(self, root: TreeNode):
        self.root = root

    def longest_path_in_tree(self) -> int:
        if not self.root:
            return 0
        return self.longest_path_recur(self.root, 1)
    
    def longest_path_recur(self,root,cur_longest) -> int:
        longest = cur_longest
        for child in root.children:
            if child.data == root.data+1:
                longest = max(longest, self.longest_path_recur(child, cur_longest+1))
            longest = max(longest, self.longest_path_recur(child, 1))

        return longest





