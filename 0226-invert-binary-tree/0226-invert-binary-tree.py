# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:  # base case: null node
            return None

        # recursive case: recursively invert left & right subtrees
        l_inverted = self.invertTree(root.left)
        r_inverted = self.invertTree(root.right)

        # swapping left and right child nodes
        root.left = r_inverted
        root.right = l_inverted

        # returns current subtree
        return root

        # final notes:
        # DFS -> traverses all the way down to leaves
        # bottom-up -> swaps child nodes after being processed by DFS
