# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # split
        odd, even = None, None
        oddCurrent, evenCurrent = None, None
        flag = True
        now = head
        while now:
            temp = now
            now = now.next
            temp.next = None

            if flag:
                if oddCurrent:
                    oddCurrent.next = temp
                    oddCurrent = oddCurrent.next
                else:
                    oddCurrent = temp
                    odd = temp
            else:
                if evenCurrent:
                    evenCurrent.next = temp
                    evenCurrent = evenCurrent.next
                else:
                    evenCurrent = temp
                    even = temp

            flag = not flag

        # merge
        if oddCurrent:
            oddCurrent.next = even
            
        return odd
            
            