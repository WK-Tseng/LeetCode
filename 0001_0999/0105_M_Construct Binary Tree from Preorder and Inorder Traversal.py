# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node = None
        
        if inorder:
            root = preorder.pop(0)
            root_idx_in_inorder = inorder.index(root)
            node = TreeNode(
                root, 
                self.buildTree(preorder, inorder[:root_idx_in_inorder]),
                self.buildTree(preorder, inorder[root_idx_in_inorder+1:])
                )
        
        return node