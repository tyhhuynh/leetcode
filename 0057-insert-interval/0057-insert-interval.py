class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []
        i = 0

        # append intervals < newInterval[0]
        while i < len(intervals) and intervals[i][1] < newInterval[0]: 
            result.append(intervals[i])
            i += 1

        # merge newInterval w/ overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        result.append(newInterval)
        # NOTE: second condition of while-loops keeps i on correct index

        # append the rest of the intervals
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        
        return result