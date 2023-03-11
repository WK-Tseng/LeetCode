# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def find_root_node(node, end):
            if node == end:
                return None

            fast, slow = node, node
            while fast.next != end and fast.next.next != end:
                fast = fast.next.next
                slow = slow.next
            
            root = TreeNode(slow.val)
            root.left = find_root_node(node, slow)
            root.right = find_root_node(slow.next, end)
            return root
        
        return find_root_node(head, None)