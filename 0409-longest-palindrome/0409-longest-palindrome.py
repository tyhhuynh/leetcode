class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = dict()
        length = 0
        used_center = False

        for c in s:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1
        
        for count in counter.values():
            length += (count // 2)*2 # adds max # of characters that can be used to attain symmetry
            if count % 2 == 1: # length % 2 == 0, but one more char can be added and retain symmetry
                used_center = True
        
        if used_center:
            length += 1

        return length