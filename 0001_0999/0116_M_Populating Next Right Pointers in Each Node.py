"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        layer = [root, None]
        while layer[0]:
            tempLayer = []
            for i in range(0, len(layer) - 1):
                layer[i].next = layer[i+1]
                tempLayer.append(layer[i].left)
                tempLayer.append(layer[i].right)

            tempLayer.append(None)
            layer = tempLayer

        return root