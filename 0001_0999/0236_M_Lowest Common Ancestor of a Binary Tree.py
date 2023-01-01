# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def DFS(root, target, path):
            if root:
                if root == target:
                    path.append(root)
                    # path.append(root.val)
                    return

                DFS(root.left, target, path)

                if len(path) > 0:
                    path.append(root)
                    # path.append(root.val)
                    return

                DFS(root.right, target, path)

                if len(path) > 0:
                    path.append(root)
                    # path.append(root.val)
                    return
        
        p_path = []
        q_path = []
        DFS(root, p, p_path)
        DFS(root, q, q_path)

        # print(p_path)
        # print(q_path)

        while len(p_path) > len(q_path):
            p_path.pop(0)

        while len(q_path) > len(p_path):
            q_path.pop(0)

        for i, j in zip(p_path, q_path):
            if i == j:
                return i

        return None
            
            