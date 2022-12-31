# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        left, right = 0, len(nums) - 1
        mid = (left + right) // 2

        if right == -1:
            return None

        return TreeNode(
                nums[mid],
                self.sortedArrayToBST(nums[:mid]),
                self.sortedArrayToBST(nums[mid+1:])
                )