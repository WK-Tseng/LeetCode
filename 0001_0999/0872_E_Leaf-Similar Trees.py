# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def DFS(root, resultList):
            if root:
                left = DFS(root.left, resultList)
                right = DFS(root.right, resultList)
                if left is None and right is None:
                    resultList.append(root.val)
                return root.val
            else:
                return None

        list1 = []
        list2 = []
        DFS(root1, list1)
        DFS(root2, list2)
        
        return list1 == list2