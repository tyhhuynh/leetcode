class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda i : i[0]) # check meeting-rooms.py code
        result = [intervals[0]]

        for start, end in intervals[1:]:
            iEnd = result[-1][1] # end value of most recently added element in result

            if start <= iEnd:
                result[-1][1] = max(iEnd, end) # [1,5], [2,4]
            else:
                result.append([start, end]) # [1,5], [7,8]
        
        return result
