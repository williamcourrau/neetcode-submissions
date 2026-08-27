# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count_good_nodes = 0
        def dfs(root, max_path):
            nonlocal count_good_nodes
            
            if root is None:
                return max_path
            
            if root.val >= max_path:
                count_good_nodes += 1

            max_current = max(root.val, max_path)
            dfs(root.left, max_current)
            dfs(root.right, max_current)
        
        dfs(root, root.val)
        return count_good_nodes
        