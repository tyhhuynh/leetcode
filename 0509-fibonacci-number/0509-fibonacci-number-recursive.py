class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        # base case:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # return cached result if already computed
        if n in self.memo:
            return self.memo[n]
        
        # recursive case: compute and store result in memo
        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]

    def __init__(self):
        self.memo = {} # memoization dict to cache previously computed fib values
