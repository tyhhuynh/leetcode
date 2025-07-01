class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        check = dict()

        for c in magazine:
            if c not in check:
                check[c] = 1
            else:
                check[c] += 1
        
        for c in ransomNote:
            if c not in check or check[c] == 0: # char DNE or used up
                return False
            else:
                check[c] -= 1
        return True