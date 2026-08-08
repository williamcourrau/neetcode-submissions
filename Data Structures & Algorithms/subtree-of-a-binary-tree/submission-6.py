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
        
        def isSameTree(s, t):
            if s is None and t is None:
                return True
            if s is None or t is None:
                return False
            if s.val != t.val:
                return False
            return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        if isSameTree(root, sub_root):
            return True

        return self.isSubtree(root.left, sub_root) or self.isSubtree(root.right, sub_root)
        
        
        