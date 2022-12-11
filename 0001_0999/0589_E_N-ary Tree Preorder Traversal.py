"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # def preorder(self, root: 'Node') -> List[int]:
    #     def DFS(root):
    #         result = []
    #         if root:
    #             result.append(root.val)
    #             for child in root.children:
    #                 result += DFS(child)
    #         return result
    #     return DFS(root)

    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def DFS(root):
            if root:
                result.append(root.val)
                for child in root.children:
                    DFS(child)
        DFS(root)
        return result


            