
# 🧮 Problem 35: Implement a basic queue using an array or list
# --------------------------------------------------
# Problem Statement:
# Implement a queue data structure using a Python list.
#
# The queue should support the following operations:
# - enqueue(x): Add element x to the rear of the queue.
# - dequeue(): Remove and return the front element of the queue.
# - peek(): Return the front element without removing it.
# - is_empty(): Check if the queue is empty.
#
# Example:
# Input: enqueue(1), enqueue(2), dequeue(), peek()
# Output: 1, 2

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None  # or raise exception

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0


# Example usage
queue  = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())
print(queue.peek())


