# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid # reduces r-side except mid b/c mid could be 1st bad version
            else:
                l = mid + 1 # reduces l-side including mid b/c it's all good version, so check next iteration
        return l # can return r bc they are equal