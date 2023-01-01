# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            if not root.right:
                return root.left
            
            if not root.left:
                return root.right

            min_node = root.right
            while min_node.left:
                min_node = min_node.left
            
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root