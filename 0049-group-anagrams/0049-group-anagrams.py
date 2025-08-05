class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list) # mapping character count to list of anagrams
        # result = (0, ... ,0): ["for", "example"]

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            result[tuple(count)].append(s) # creates either a new key if DNE & or adds to existing key's value
        
        return result.values()