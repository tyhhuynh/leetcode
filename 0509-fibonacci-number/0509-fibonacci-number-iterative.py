class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        a, b = 0, 1
        
        # base case:
        if n <= 0: # returns 0 if n is 0 || negative
            return a
            
        # iterative case: compute fib value bottom-up
        for i in range(n - 1): # index i does not matter, # of iterations does
            a, b = b, a + b
        return b
