# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        now = head
        val_dict = {}

        while now:
            val_dict[now.val] = val_dict.get(now.val, 0) + 1
            now = now.next

        result = None
        now = head
        while now:
            if val_dict[now.val] == 1:
                if result:
                    result.next = now
                    result = result.next
                else:
                    head = now
                    result = now

            now = now.next

            if result:
                result.next = None

        if not result:
            head = None
        return head