# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hA, hB = headA, headB
        hA_len, hB_len = 1, 1

        while hA.next:
            hA = hA.next
            hA_len += 1
        
        while hB.next:
            hB = hB.next
            hB_len += 1

        if hA != hB:
            return None

        while hA_len > hB_len:
            headA = headA.next
            hA_len -= 1

        while hB_len > hA_len:
            headB = headB.next
            hB_len -= 1

        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None