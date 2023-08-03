# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        while head:
            _next = head.next
            head.next = pre
            pre = head
            head = _next
        head = pre
        return head

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        tmp = head

        pre = None
        startPre = None
        start = None
        end = None
        count = 1
        while tmp:
            if count == left:
                startPre = pre
                start = tmp

            if count == right:
                end = tmp
                break

            pre = tmp
            tmp = tmp.next
            count += 1

        if start and end:
            endNext = end.next
            end.next = None

            tmp = self.reverseList(start)
            if startPre:
                startPre.next = tmp
            else:
                head = tmp

            start.next = endNext

        return head