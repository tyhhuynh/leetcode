class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c in closeToOpen: # closing brackets
                if stack and stack[-1] == closeToOpen[c]: # stack !empty && top of stack matches opening bracket for c
                    stack.pop()
                else:
                    return False
            else: # opening brackets
                stack.append(c)
        return True if not stack else False