class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # reverse bucket sort:
        # i.e. nums = [1, 1, 1]
        count = {} # frequency map -> {1: 3}
        frequency = [[] for i in range(len(nums) + 1)] # initializes nested list with n + 1 empty lists
        # index = frequency of num
        # value = num from nums

        # construction of frequency map of nums
        for num in nums:
            count[num] = 1 + count.get(num, 0) # current count || 0 if not present
        
        # places correct num in frequency bucket
        for num, c in count.items():
            frequency[c].append(num)
        
        result = []

        for i in range(len(frequency) -1, 0, -1): # loop backwards b/c last index is largest
            for n in frequency[i]: # skips if frequency[i] == []
                result.append(n) 
                if len(result) == k:
                    return result