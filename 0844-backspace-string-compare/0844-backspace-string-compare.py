class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1 # traverse in reverse
        
        # helper fn:
        def backspace_char(s: str, index: int) -> int:
            skip = 0 # #-counter
            while index >= 0:
                if s[index] == "#":
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else: # skip == 0 & s[index] != "#"
                    break # break out of while loop and return index
                index -= 1 # applies "backspace" if skip == 1
            return index # index = index of next valid char
        
        while i >= 0 or j >= 0:
            i = backspace_char(s, i)
            j = backspace_char(t, j)

            # both strings were exhausted: length of strings are equal & chars match
            if i < 0 and j < 0:
                return True
            
            # length of strings are not equal || char of strings do not match
            if i < 0 or j < 0 or s[i] != t[j]:
                return False

            i -= 1
            j -= 1

        return True