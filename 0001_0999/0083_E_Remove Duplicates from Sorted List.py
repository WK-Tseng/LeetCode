# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        last = head
        node = head.next

        while node:
            if node.val == last.val:
                last.next = node.next
            else:
                last = node
            node = node.next

        return head