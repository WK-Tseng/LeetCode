# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getNextNode(head, cost = 1):
            if cost == 0 or head is None:
                return head
            
            return getNextNode(head.next, cost-1)
        
        def swap(head: Optional[ListNode], k):
            tempList = []
            for i in range(k):
                tempList.append(getNextNode(head, i))
                
                if tempList[i] is None:
                    return head
            
            tempAllnext = tempList[-1].next
            tempList = tempList[::-1]
            
            for i in range(k-1):
                tempList[i].next = tempList[i+1]
            
            tempList[-1].next = tempAllnext
            
            return tempList[0]

        
        
        head = swap(head, k)
        lastNode = getNextNode(head, k-1)
        nowNode = None
        if not (lastNode is None):
            nowNode = lastNode.next
        
        # print(head)
        # print(nowNode)
        
        while nowNode:
            nowNode = swap(nowNode, k)
            lastNode.next = nowNode
            
            lastNode = getNextNode(lastNode, k)
            if lastNode is None:
                nowNode = None
            else:
                nowNode = lastNode.next
            
            
        return head