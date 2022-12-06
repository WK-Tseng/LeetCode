# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow: f + a
        # fast: f + a + b + a
        # 2 * (f + a) = f + a + b + a
        # 2f + 2a = f + 2a + b
        # f = b

        # run, slow: f + a, fast: f + a + b + a
        flag = False
        slow, fast = head, head
        while fast and fast.next and (not flag):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True

        # run f = b
        if flag:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
                
            return slow

        return None