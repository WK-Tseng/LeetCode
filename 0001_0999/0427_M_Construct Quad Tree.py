"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def split_grid(x1, x2, y1, y2):
            if x2 - x1 != 1:
                xn = (x1+x2)//2
                yn = (y1+y2)//2

                topLeftNode = split_grid(x1, xn, y1, yn)
                topRightNode = split_grid(xn, x2, y1, yn)
                bottomLeftNode = split_grid(x1, xn, yn, y2)
                bottomRightNode = split_grid(xn, x2, yn, y2)

                if topLeftNode.isLeaf and topRightNode.isLeaf and bottomLeftNode.isLeaf and bottomRightNode.isLeaf and \
                topLeftNode.val == topRightNode.val and topLeftNode.val == bottomLeftNode.val and topLeftNode.val == bottomRightNode.val:
                    return  Node(topLeftNode.val, 1, None, None, None, None)
                else:
                    return Node(1, 0, topLeftNode, topRightNode, bottomLeftNode, bottomRightNode)
            
            else:
                return Node(grid[y1][x1], 1, None, None, None, None)

        n = len(grid)
        return split_grid(0, n, 0, n)