# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        data_dict = {}
        data_flag = collections.defaultdict(int)
        result = []

        def DFS(node):
            if node:
                data = (node.val, DFS(node.left), DFS(node.right))
                if data not in data_dict:
                    data_dict[data] = len(data_dict) + 1
                idx = data_dict[data]
                data_flag[idx] += 1
                if data_flag[idx] == 2:
                    result.append(node)
                return idx

            return 0

        DFS(root)

        return result