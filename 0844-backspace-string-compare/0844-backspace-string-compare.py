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
                else:
                    break
                index -= 1
            return index
        
        while i >= 0 or j >= 0:
            i = backspace_char(s, i)
            j = backspace_char(t, j)

            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0 or s[i] != t[j]:
                return False

            i -= 1
            j -= 1
        return True
