class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base case:
        a, b = 0, 1
        if n <= 0:
            return a

        # recursive case:
        for i in range(2, n + 1):
            a, b = b, a + b
        return b