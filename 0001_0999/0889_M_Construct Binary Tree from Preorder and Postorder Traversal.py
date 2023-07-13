# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def func(pre, post):
            
            if not pre:
                return None
            
            if len(pre) == 1:
                return TreeNode(post.pop())

            node = TreeNode(post.pop())
            idx = pre.index(post[-1])

            node.right = func(pre[idx:], post)
            node.left = func(pre[1:idx], post)

            return node

        return func(preorder, postorder)