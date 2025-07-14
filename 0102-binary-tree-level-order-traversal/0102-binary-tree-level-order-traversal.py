# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []
        q = deque()
        q.append(root) # initialize queue with root

        # BFS
        while q: # while q is NOT empty
            q_length = len(q)
            level = []
            for i in range(q_length):
                node = q.popleft()
                if node: # checks if node is NOT NULL
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level: # NULL nodes should not be in result
                result.append(level)
        
        return result
        