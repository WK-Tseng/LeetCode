# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            if low <= root.val <= high:
                return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
            elif root.val < low:
                return self.rangeSumBST(root.right, low, high)
            elif root.val > high:
                return self.rangeSumBST(root.left, low, high)
        else:
            return 0

    # AC
    # def sumTree(self, root):
    #     if root:
    #         return root.val + self.sumTree(root.left) + self.sumTree(root.right)
    #     else:
    #         return 0

    # def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
    #     resultLeft = 0
    #     resultRight = 0
        
    #     # Find range root
    #     while not (low <= root.val <= high):
    #         if root.val > high:
    #             root = root.left
    #         elif root.val < low:
    #             root = root.right
    #     # print(root.val)

    #     # sum root to low (left)
    #     leftPoint = root
    #     while leftPoint.val != low:
    #         if leftPoint.val > low:
    #             resultLeft += leftPoint.val
    #             if leftPoint != root:
    #                 resultLeft += self.sumTree(leftPoint.right)
    #             leftPoint = leftPoint.left
    #         else:
    #             leftPoint = leftPoint.right

    #     resultLeft += leftPoint.val
    #     if leftPoint != root:
    #         resultLeft += self.sumTree(leftPoint.right)
    #     # print(resultLeft)

    #     # sum root to high (right)
    #     rightPorint = root
    #     while rightPorint.val != high:
    #         if rightPorint.val > high:
    #             rightPorint = rightPorint.left
    #         else:
    #             resultRight += rightPorint.val
    #             if rightPorint != root:
    #                 resultRight += self.sumTree(rightPorint.left)
    #             rightPorint = rightPorint.right

    #     resultRight += rightPorint.val 
    #     if rightPorint != root:
    #         resultRight += self.sumTree(rightPorint.left)
    #     # print(resultRight)
        
    #     # add root two times, so subtract once.
    #     return resultLeft + resultRight - root.val