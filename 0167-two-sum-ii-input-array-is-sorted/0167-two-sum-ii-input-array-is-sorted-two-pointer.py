class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(numbers)):
            hash[numbers[i]] = i
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in hash and hash[complement] != i:
                return [i + 1, hash[complement] + 1]
