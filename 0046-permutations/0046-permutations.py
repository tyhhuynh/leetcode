class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # iterative solution
        
        perms = [[]] # base case

        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = list(p) # .copy() for Py3
                    p_copy.insert(i, n) # insert value at all possible indicies of p
                    new_perms.append(p_copy)
            perms = new_perms
        return perms