class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        result = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            result = max(result, area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else: # height[l] == height[r]
                if height[l + 1] > height[r - 1]:
                    l += 1
                else:
                    r -= 1
        return result

            