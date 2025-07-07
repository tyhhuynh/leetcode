class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        current = 0

        for num in nums:
            current += num
            maxSum = max(maxSum, current)
            if current < 0:
                current = 0 # reset current to 0

        return maxSum