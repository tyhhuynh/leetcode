class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = dict()
        n = len(nums)
        
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        
        for k,v in counter.items():
            if v > n // 2:
                return k