# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def swap(head: Optional[ListNode]):
            if head:
                if head.next:
                    headTemp = head
                    nextTemp = head.next
                    nextTemp2 = head.next.next

                    head = nextTemp
                    head.next = headTemp
                    head.next.next = nextTemp2
            
            return head
            
        
        head = swap(head)
        
#         tempList = []
        
        if head:
            if head.next:
                lastNode = head.next
                tempNode = head.next.next
                
                while tempNode:
                    tempNode = swap(tempNode)
                    lastNode.next = tempNode
                    
                    lastNode =  tempNode.next
                    tempNode = tempNode.next
                    if tempNode:
                        tempNode = tempNode.next


        return head
            