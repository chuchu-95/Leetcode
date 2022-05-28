# class MyQueue:
#     def __init__(self):
#         self.stackOne = []  # first add
#         self.stackTwo = []

#     def push(self, x: int) -> None:
#         while self.stackTwo:
#             self.stackOne.append(self.stackTwo.pop())
#         self.stackOne.append(x)

#     def pop(self) -> int:
#         while self.stackOne:
#             self.stackTwo.append(self.stackOne.pop())
#         return self.stackTwo.pop()

#     def peek(self) -> int:
#         while self.stackOne:
#             self.stackTwo.append(self.stackOne.pop())
#         return self.stackTwo[-1]

#     def empty(self) -> bool:
#         if not self.stackOne and not self.stackTwo:
#             return True
#         return False



# # Your MyQueue object will be instantiated and called as such:
# # obj = MyQueue()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.peek()
# # param_4 = obj.empty()


class MyQueue:
    
    def __init__(self):
        self.inStack, self.outStack = [], []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.outStack.pop()

    def peek(self) -> int:
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self) -> bool:
        if not self.inStack and not self.outStack:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()