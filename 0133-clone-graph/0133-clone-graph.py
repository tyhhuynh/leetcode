"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldToNew = {}

        def clone(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val) # creates new node object w/ same value as og node
            oldToNew[node] = copy # stores the mapping of og node to its clone to avoid revisiting & cycles

            # appends neighbors onto copy node
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy
        
        return clone(node) if node else None
