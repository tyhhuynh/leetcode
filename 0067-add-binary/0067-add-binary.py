class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        sum = []

        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            total = bit_a + bit_b + carry
            sum.append(str(total % 2))
            carry = total // 2

            i -= 1
            j -= 1
        
        return ''.join(reversed(sum)) # concatenates elements from reversed(list) into empty str

