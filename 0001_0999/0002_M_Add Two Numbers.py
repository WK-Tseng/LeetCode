# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1 = l1
        num_2 = l2
        AnsList = []
        thisNode = None
        nextNode = None
        
        while not(num_1 is None and num_2 is None):
            tempVal = 0
            
            thisNode = nextNode
            nextNode = None
            
            if not thisNode is None:
                tempVal = thisNode.val
            
            if not num_1 is None:
                tempVal += num_1.val
                num_1 = num_1.next
            
            if not num_2 is None:
                tempVal += num_2.val
                num_2 = num_2.next
            
            if tempVal >= 10:
                nextNode = ListNode(val=1)
                tempVal -= 10
            
            if thisNode is None:
                thisNode = ListNode(val=tempVal)
            else:
                thisNode.val = tempVal
            
            AnsList.append(thisNode)
        
        if not nextNode is None:
            AnsList.append(nextNode)
                
        for i in range(len(AnsList) - 1):
            AnsList[i].next = AnsList[i+1]
            
            
        return AnsList[0]