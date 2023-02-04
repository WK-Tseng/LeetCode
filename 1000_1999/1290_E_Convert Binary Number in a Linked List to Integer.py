# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin_str_list = []
        while head:
            bin_str_list.append(str(head.val))
            head = head.next
        
        return int(''.join(bin_str_list), 2)