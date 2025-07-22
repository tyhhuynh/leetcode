# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        def validate(node, left, right):
            # base case:
            if not node:
                return True
            
            # checks if nodes are out of bounds
            if not (node.val < right and node.val > left):
                return False
            
            # recursive case:
            return (validate(node.left, left, node.val) and validate(node.right, node.val, right))
        
        return validate(root, float("-inf"), float("inf"))
