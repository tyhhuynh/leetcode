class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        for i, a in enumerate(nums): # index, 1st value
            if i > 0 and a == nums[i - 1]: # skips value if duplicate
                continue
            
            l, r = i + 1, len(nums) - 1

            # 2Sum II 2-Pointer Implementation
            while l < r:
                total = a + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: # continues to increment left pointer until value isn't duplicate
                        l += 1
            
        return result