class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = [] # s
        b = [] # t

        for c in s:
            if c == "#":
                a.pop() if a else None
            else:
                a.append(c)
        
        for c in t:
            if c == "#":
                b.pop() if b else None
            else:
                b.append(c)

        return a == b