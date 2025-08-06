class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s # [length of string]#[string]
        return result

    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#": # finds the "#" marker which denotes start of string
                j += 1
            length = int(s[i:j]) # sets variable length to the length of string
            result.append(s[j + 1: j + 1 + length]) # j+1: after "#" marker, j+1+length: excludes last index
            i = j + 1 + length # updates i s.t. j can point to next marker
        return result
