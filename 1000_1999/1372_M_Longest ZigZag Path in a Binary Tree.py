# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        flag = []
        maxPath = [0]

        def DFS(root):
            if root:
                if len(flag) == 0:
                    flag.append([1, -1])
                    DFS(root.left)
                    flag.pop(-1)
                elif flag[-1][1] == 1:
                    flag.append([flag[-1][0]+1, -1])
                    DFS(root.left)
                    flag.pop(-1)
                else:
                    flag.append([1, -1])
                    DFS(root.left)
                    flag.pop(-1)

                if len(flag) == 0:
                    flag.append([1, 1])
                    DFS(root.right)
                    flag.pop(-1)
                elif flag[-1][1] == -1:
                    flag.append([flag[-1][0]+1, 1])
                    DFS(root.right)
                    flag.pop(-1)
                else:
                    flag.append([1, 1])
                    DFS(root.right)
                    flag.pop(-1)
            else:
                temp = flag[:-1]
                if len(temp) > 0:
                    maxPath[0] = max(maxPath[0], temp[-1][0])

        DFS(root)

        return maxPath[0]
