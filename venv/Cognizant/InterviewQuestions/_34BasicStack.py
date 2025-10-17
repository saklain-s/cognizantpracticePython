
# 🧮 Problem 35: Implement a basic stack using an array or list
# --------------------------------------------------
# Problem Statement:
# Implement a stack with the following operations using a Python list:
# - push(x): Add element x to the top of the stack
# - pop(): Remove and return the top element of the stack
# - peek(): Return the top element without removing it
# - is_empty(): Return True if the stack is empty, False otherwise
#
# Example:
# stack = Stack()
# stack.push(5)
# stack.push(10)
# stack.pop()     # Returns 10
# stack.peek()    # Returns 5
# stack.is_empty() # Returns False
#
# Expected:
# - Implement your own stack class with these methods
# - Do not use Python's built-in stack modules like `queue` or `collections.deque`

class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None  # or raise exception

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


# Example usage
stack = Stack()
stack.push(5)
stack.push(10)
print(stack.pop())      # Output: 10
print(stack.peek())     # Output: 5
print(stack.is_empty()) # Output: False

