# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        sub_left = self._traverseTree(root.left)
        sub_right = self._traverseTree(root.right)
        if abs(sub_left - sub_right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def _traverseTree(self, root) -> int:
        # count the node per sub_tree left + right
        if root is None:
            return 0

        return 1 + max(self._traverseTree(root.left), self._traverseTree(root.right))
        
