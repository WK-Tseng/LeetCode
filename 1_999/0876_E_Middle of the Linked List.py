# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        now = head
        while now:
            now = now.next
            count += 1
        
        count //= 2

        now = head
        for _ in range(count):
            now = now.next

        return now