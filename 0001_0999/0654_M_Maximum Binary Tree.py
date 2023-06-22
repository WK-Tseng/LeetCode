# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        stack = []
        for num in nums:
            node = TreeNode(num)
            lastNode = None

            while stack and stack[-1].val < num:
                lastNode = stack.pop(-1)
            node.left = lastNode

            if stack:
                stack[-1].right = node
            
            stack.append(node)

        return stack[0]