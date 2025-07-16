class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        result = 0
        stack = deque()

        if len(tokens) == 1:
            return int(tokens[0])

        for i in tokens:
            if i == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                result = a + b
                stack.append(str(result))
            
            elif i == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                result = a - b
                stack.append(str(result))

            elif i == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                result = a * b
                stack.append(str(result))

            elif i == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                result = int(float(a) / b) # truncate toward 0, not floor division
                stack.append(result)

            else: 
                stack.append(int(i))

        return result
