# 🧮 Problem 28: Merge two sorted linked lists
# --------------------------------------------------
# Problem Statement:
# Given two sorted linked lists, merge them into a single sorted linked list.
#
# Example:
# Input:  l1 = 1 -> 3 -> 5, l2 = 2 -> 4 -> 6
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
#
# Expected:
# - Implement the merging logic manually (do not convert to arrays and sort).
# - Maintain the sorted order while merging.
# - You can solve it iteratively or recursively.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative approach to merge two sorted linked lists
def merge_two_lists(l1, l2):
    dummy = ListNode(0)  # Dummy node to simplify code
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Append the remaining nodes
    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return dummy.next

# Helper function to create a linked list from a Python list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(" -> ".join(map(str, res)))

# Example usage:
l1 = create_linked_list([1, 3, 5])
l2 = create_linked_list([2, 4, 6])
merged = merge_two_lists(l1, l2)
print_linked_list(merged)  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
