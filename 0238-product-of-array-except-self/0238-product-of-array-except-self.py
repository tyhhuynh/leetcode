class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    
        products = [1] * len(nums)

        # update products L-R
        prefix = 1
        for i in range(len(nums)):
            products[i] = prefix
            prefix *= nums[i]

        # update products R-L
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= postfix
            postfix *= nums[i]

        return products
            
        