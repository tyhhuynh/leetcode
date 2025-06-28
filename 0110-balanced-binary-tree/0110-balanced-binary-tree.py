# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # helper fn
        def check(node) -> Tuple[bool, int]:
            
            # base case
            if node is None:
                return True, 0
            
            # recursive case
            l_balanced, l_height = check(node.left)
            r_balanced, r_height = check(node.right)

            # balanced iff both subtrees are balanced & height difference at most 1
            balanced = l_balanced and r_balanced and abs(l_height - r_height) <= 1

            height = 1 + max(l_height, r_height) # adds height of max subtree onto current node

            return balanced, height
        
        return check(root)[0] # boolean value in tuple