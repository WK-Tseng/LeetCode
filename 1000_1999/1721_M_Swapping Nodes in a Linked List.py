# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        for _ in range(1, k):
            first = first.next

        last = head
        endCheck = first
        while endCheck.next:
            last = last.next
            endCheck = endCheck.next

        first.val, last.val = last.val, first.val
        return head