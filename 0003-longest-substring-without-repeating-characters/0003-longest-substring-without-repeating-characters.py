class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = dict()
        start = 0
        max_length = 0

        for i, char in enumerate(s): # enumerate() -> [index, element]
            if char in substrings and substrings[char] >= start: # checks if char is within current substring
                start = substrings[char] + 1 # resets start pointer
            substrings[char] = i # updates most recent location (index) of char
            max_length = max(max_length, i - start + 1) 
        return max_length
