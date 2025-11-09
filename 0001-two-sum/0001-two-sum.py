class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brute force: O(n^2)
        # for i in range(0, len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # hashmap solution: O(n)
        hash = {}
        
        for i in range(len(nums)):
            hash[nums[i]] = i # {element: index}
            

        for i in range(len(nums)):
            complement = target - nums[i] # target - element
            if complement in hash and hash[complement] != i: # complement exists as element in hash & its index is not duplicate
                return [i, hash[complement]]
        return []
        
