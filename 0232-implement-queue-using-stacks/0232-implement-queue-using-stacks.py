class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack: # if out_stack = empty
            while self.in_stack:
                value = self.in_stack.pop() # last value appended
                self.out_stack.append(value) # adds last value of in_stack to out_stack (bottom)
        return self.out_stack.pop() # returns first element appended in in_stack

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                value = self.in_stack.pop()
                self.out_stack.append(value)
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()