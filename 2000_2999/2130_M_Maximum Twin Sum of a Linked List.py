# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        first = head
        while first:
            first = first.next
            n += 1

        halfN = n // 2
        first = head
        stack = []
        for _ in range(halfN):
            stack.append(first.val)
            first = first.next
        
        result = 0
        for _ in range(halfN):
            result = max(result, first.val + stack.pop(-1))
            first = first.next

        return result