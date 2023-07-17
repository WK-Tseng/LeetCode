# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = l1
        str1 = ""
        while temp:
            str1 += str(temp.val)
            temp = temp.next

        temp = l2
        str2 = ""
        while temp:
            str2 += str(temp.val)
            temp = temp.next

        resultStr = str(int(str1) + int(str2))
        resultList = [int(s) for s in resultStr]

        root = ListNode(val=resultList.pop(0))
        temp = root
        while resultList:
            temp.next = ListNode(val=resultList.pop(0))
            temp = temp.next

        return root