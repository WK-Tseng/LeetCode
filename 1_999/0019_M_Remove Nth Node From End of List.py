# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tempList = []
        tempNode = head
        
        while tempNode != None:
            tempList.append(tempNode)
            
            if len(tempList) > n+1:
                tempList.pop(0)
            
            tempNode = tempNode.next
        
        # print(len(tempList))
        # print(tempList)
        
        tempListLen = len(tempList)
        
        if tempListLen >= n:
            if n == 1:
                if tempListLen == 1:
                    head = None
                elif tempListLen > 1:
                    tempList[-2].next = None
            elif tempListLen == n:
                head = head.next
            elif tempListLen > n:
                tempList[0].next = tempList[2]
                    
                
        return head
            