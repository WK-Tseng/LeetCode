# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        nowNode = head
        lastNode = None

        splitNode = [None, None]
        splitNodeFlag = False

        while nowNode:
            if not splitNodeFlag:
                if nowNode.val >= x:
                    splitNode = [lastNode, nowNode]
                    splitNodeFlag = True
            else:
                if nowNode.val < x:
                    lastNode.next = nowNode.next
                    nowNode.next = splitNode[1]
                    if splitNode[0]:
                        splitNode[0].next = nowNode
                    else:
                        head = nowNode
                    splitNode[0] = nowNode
                    

            lastNode = nowNode
            nowNode = nowNode.next

        return head
            
