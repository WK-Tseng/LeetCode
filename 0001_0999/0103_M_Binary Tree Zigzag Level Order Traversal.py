# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]
        flag = True

        while queue:
            result.append([node.val for node in queue])
            if flag:
                result[-1] = result[-1][::-1]
            flag = not flag

            next_queue = []
            for node in queue:
                if node.right:
                    next_queue.append(node.right)
                if node.left:
                    next_queue.append(node.left)

            
            queue = None
            if len(next_queue) > 0:
                queue = next_queue

        return result
            