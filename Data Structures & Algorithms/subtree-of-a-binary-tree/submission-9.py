# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if not sub_root:
            return True
        
        def dfs(r, s):
            if r is None and s is None:
                return True
            
            if r is None or s is None:
                return False
            
            if r.val != s.val:
                return False
            
            return dfs(r.left, s.left) and dfs(r.right, s.right)

        if dfs(root, sub_root):
            return True

        return self.isSubtree(root.left, sub_root) or self.isSubtree(root.right, sub_root)
        
        
        