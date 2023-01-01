# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        path = []
        def DFS(root):
            if root:
                path.append(str(root.val))
                DFS(root.left)
                DFS(root.right)
            else:
                path.append('#')

        DFS(root)
        return ','.join(path)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self._data = data
        if data[0] == '#':
            return None
        else:
            node = TreeNode(int(self._data[:self._data.index(',')]))
            node.left = self.deserialize(self._data[self._data.index(',')+1:])
            node.right = self.deserialize(self._data[self._data.index(',')+1:])
            return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))