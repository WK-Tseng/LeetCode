# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        now = head
        last = None
        while now:
            if now.val == val:
                if last:
                    last.next = now.next
                else:
                    head = now.next
                    last = None
            else:
                last = now
            now = now.next
        return head