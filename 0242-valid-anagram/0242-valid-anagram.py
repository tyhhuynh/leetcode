class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # initalize empty hash map - char:frequency
        check = dict()
        
        # increments freq of char
        for c in s:
            if c not in check:
                check[c] = 1
            else:
                check[c] += 1

        # decrements freq of char
        for c in t:
            if c not in check:
                return False
            else:
                check[c] -= 1
        
        # s & t are anagrams if freq == 0 for all chars
        for count in check.values():
            if count != 0:
                return False
        return True