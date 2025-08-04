https://www.lintcode.com/problem/920/ # LeetCode premium problem

# Definition of Interval:
# class Interval(object):
#    def __init__(self, start, end):
#        self.start = start
#        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start) # sorts the list of intervals in ascending order based on interval.start
        # lambda fn: takes in i and outputs i.start value
        # sort(key = lambda fn): sorts i.start value appropriately

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1] # index starts at 1 instead of 0
            i2 = intervals[i]

            if i1.end > i2.start: # end time of i1 overlaps with start time of i2
                return False
        return True
