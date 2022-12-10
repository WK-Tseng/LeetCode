# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # AC
    # def treeSum(self, root):
    #     return root.val + self.treeSum(root.left) + self.treeSum(root.right) if root else 0

    # def maxTreeProduct(self, root, treeSum, product=0):
    #     if root:
    #         left = self.maxTreeProduct(root.left, treeSum, product)
    #         right = self.maxTreeProduct(root.right, treeSum, product)
    #         tempSum = root.val + left[1] + right[1]
    #         product = max((treeSum - tempSum) * tempSum, left[0], right[0])
    #         return product, tempSum
    #     else:
    #         return 0, 0

    # def maxProduct(self, root: Optional[TreeNode]) -> int:
    #     return self.maxTreeProduct(root, self.treeSum(root))[0] % (10**9 + 7)

    # AC
    def treeSum(self, root, treeSumList):
        if root:
            sumVal = root.val + self.treeSum(root.left, treeSumList) + self.treeSum(root.right, treeSumList)
            treeSumList.append(sumVal)
            return sumVal
        else:
            return 0

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        treeSumList = []
        treeSum = self.treeSum(root, treeSumList)
        return max(i * (treeSum - i) for i in treeSumList) % (10**9 + 7)