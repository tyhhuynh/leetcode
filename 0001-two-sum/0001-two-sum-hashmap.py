class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}

        for i in range(len(nums)):
            hash[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash and hash[complement] != i:
                return [i, hash[complement]]
        return []