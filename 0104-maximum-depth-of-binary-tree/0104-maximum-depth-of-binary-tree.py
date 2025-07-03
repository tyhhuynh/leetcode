# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # helper fn
        def countDepth(node):
            
            # base case:
            if node is None:
                return 0
            
            # recursive case:
            if node is not None:
                left = countDepth(node.left)
                right = countDepth(node.right)
                return 1 + max(left, right) # current node + larger subtree

        return countDepth(root)
            