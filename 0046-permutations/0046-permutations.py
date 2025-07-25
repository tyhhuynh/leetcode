class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # recursive solution

        # base case:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        result = []

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = list(p) # .copy() for Py3
                p_copy.insert(i, nums[0]) # insert value at all possible indices of p
                result.append(p_copy)
        return result