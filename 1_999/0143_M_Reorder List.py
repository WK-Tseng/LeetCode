# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # split
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        a, b = head, slow.next
        slow.next = None

        # reverse
        last = None
        while b:
            _next = b.next 
            b.next = last
            last = b
            b = _next   
        b = last

        # merge
        while b:
            take = b
            b = b.next
            take.next = None

            _next = a.next
            a.next = take
            take.next = _next
            a = _next