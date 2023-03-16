# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        level = 0
        while queue:
            next_queue = []
            flag = True
            for p in queue:
                if p.left and flag:
                    next_queue.append(p.left)
                elif p.left and not flag:
                    return False
                else:
                    flag = False

                if p.right and flag:
                    next_queue.append(p.right)
                elif p.right and not flag:
                    return False
                else:
                    flag = False
            
            if len(queue) != 2**level and next_queue:
                return False

            queue = next_queue
            level += 1
        
        return True