class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:

            # checks to see if element in s is alphanumeric
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            
            # checks if left and right pointers are !equal
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
            
        return True