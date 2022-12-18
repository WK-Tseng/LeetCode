# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head
        
        def reverse(head):
            pre = None
            next = head
            while head:
                next = head.next
                head.next = pre
                pre = head
                head = next
            return pre

        def getLen(head):
            count = 0
            while head:
                head = head.next
                count += 1
            return count

        listLen = getLen(head)

        # reverse
        newHead = reverse(head)

        # rotateRight
        for _ in range(k % listLen):
            temp = newHead
            newHead = newHead.next
            temp.next = None
            head.next = temp
            head = head.next

        # reverse
        newHead = reverse(newHead)

        return newHead