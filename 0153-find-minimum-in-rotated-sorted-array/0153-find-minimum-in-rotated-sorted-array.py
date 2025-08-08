class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        result = nums[0]

        while l <= r:
            if nums[l] < nums[r]: # current portion of array is sorted
                result = min(result, nums[l])
                break

            m = (l + r) // 2
            result = min(result, nums[m])
            
            if nums[m] >= nums[l]:
                l = m + 1
            else: # nums[m] < nums[l]
                r = m - 1

        return result
