class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {} # tracks occurrences of each char
        result = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k: # checks if window is invalid
                count[s[l]] -= 1 # decrements count of leftmost char
                l += 1 # shrink window

            result = max(result, r - l + 1)
        
        return result