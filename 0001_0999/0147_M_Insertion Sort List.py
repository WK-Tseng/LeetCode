# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        newStart = ListNode()
        node = head
        pre = newStart
        while node:
            nextNode = node.next
            while pre.next is not None and pre.next.val < node.val:
                pre = pre.next
            
            node.next = pre.next
            pre.next = node
            pre = newStart
            node = nextNode

        return newStart.next
