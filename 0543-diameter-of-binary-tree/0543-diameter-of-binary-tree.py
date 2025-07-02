# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def countEdge(node):

            # base case:
            if node is None:
                return 0
            
            # recursive case:
            left = countEdge(node.left)
            right = countEdge(node.right)
            
            self.diameter = max(self.diameter, left + right)

            # returns height, not diameteter
            return 1 + max(left, right) # edge of connected parent + height of left || right subtree
            
        countEdge(root)
        return self.diameter