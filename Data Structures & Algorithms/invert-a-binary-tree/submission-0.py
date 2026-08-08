# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return root
        
        self._invert_tree(root)

        return root
        
    
    def _invert_tree(self, root):
        if root is None:
            return 
        
        self._invert_tree(root.left)
        self._invert_tree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp


        
        