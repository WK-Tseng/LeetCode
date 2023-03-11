# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        node = head
        self.node_list = []
        while node:
            self.node_list.append(node.val)
            node = node.next

    def getRandom(self) -> int:
        return random.choice(self.node_list)

# AC, slow
# class Solution:

#     def __init__(self, head: Optional[ListNode]):
#         self.head = head

#     def getRandom(self) -> int:
#         result = 0
#         node, idx = self.head, 0
#         while node:
#             if random.randint(0, idx) == 0:
#                 result = node.val
#             node = node.next
#             idx += 1
#         return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

