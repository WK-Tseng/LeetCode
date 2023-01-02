# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1

        fill = ListNode(float('-inf'), next=head)

        step = 1
        while step < count:
            m2 = fill
            last = fill
            for _ in range(0, count, step*2):
                
                m1 = last.next
                m2 = m1
                for _ in range(step):
                    if m2 is None:
                        break
                    m2 = m2.next
                next_head = m2
                for _ in range(step):
                    if next_head is None:
                        break
                    next_head = next_head.next

                m1_count = 0
                m2_count = 0
                while m1_count < step and m2_count < step and m1 and m2:
                    if m1.val < m2.val:
                        last.next = m1
                        m1 = m1.next
                        last = last.next
                        m1_count += 1
                    else:
                        last.next = m2
                        m2 = m2.next
                        last = last.next
                        m2_count += 1

                else:
                    while m1_count < step and m1:
                        last.next = m1
                        m1 = m1.next
                        last = last.next
                        m1_count += 1

                    while m2_count < step and m2:
                        last.next = m2
                        m2 = m2.next
                        last = last.next
                        m2_count += 1
                last.next = next_head
                
            step *= 2

        return fill.next
