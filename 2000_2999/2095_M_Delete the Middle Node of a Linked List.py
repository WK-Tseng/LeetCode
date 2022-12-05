# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        now = head
        while now:
            now = now.next
            count += 1
        
        count //= 2

        now = head
        last = None
        for _ in range(count):
            last = now
            now = now.next

        if last:
            if now:
                last.next = now.next
        else:
            head = None

        return head