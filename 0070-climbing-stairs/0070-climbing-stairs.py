class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {} # cache

        def helper(k):

            # base case:
            if k == 0 or k == 1:
                return 1
            
            # return stored value if it exists
            if k in memo:
                return memo[k]
            
            # recursive case:
            elif k > 1:
                memo[k] = helper(k-1) + helper(k-2)
                return memo[k]

        return helper(n)