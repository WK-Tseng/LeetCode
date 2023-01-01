# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.iterator = []

        def DFS(root):
            if root:
                DFS(root.left)
                self.iterator.append(root.val)
                DFS(root.right)
        
        DFS(root)

    def next(self) -> int:
        return self.iterator.pop(0)

    def hasNext(self) -> bool:
        return len(self.iterator) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()