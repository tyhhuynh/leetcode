# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # # brute force: for-loop thru n: O(n)
        # for i in range(1, n + 1):
        #     if isBadVersion(i):
        #         return i

        # binary search: O(log n)
        l, r = 1, n

        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m # m COULD be 1st bad version
            else:
                l = m + 1
        return l # or r bc l == r
