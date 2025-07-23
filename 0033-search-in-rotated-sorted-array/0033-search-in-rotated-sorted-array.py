class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # binary search w/ more conditions
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # L-sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1 
                else: # target < nums[m] & target > nums[l]
                    r = m - 1
            # R-sorted portion
            else:
                if target < nums[m] or target > nums[r]: #
                    r = m - 1
                else: # target > nums[m] & target < nums[r]
                    l = m + 1
        return -1

