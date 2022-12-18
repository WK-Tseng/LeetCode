# AC, fast
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda val: val[0])
        
        result = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result

# AC, slow
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
#         def tryAdd(root, val):
#             if root:
#                 if val[1] < root.val[0]:
#                     if root.left:
#                         tryAdd(root.left, val)
#                     else:
#                         root.left = Node(val)
#                 elif val[0] > root.val[1]:
#                     if root.right:
#                         tryAdd(root.right, val)
#                     else:
#                         root.right = Node(val)
#                 else:
#                     root.val = [min(root.val[0], val[0]), max(root.val[1], val[1])]

#                     temp = getResult(root)
#                     root.val = temp[0]
#                     root.left = None
#                     root.right = None
#                     for interval in temp[1:]:
#                         tryAdd(root, interval)

#         def getResult(root, result=None):
#             if result is None:
#                 result = []

#             if root:
#                 getResult(root.left, result)
#                 result.append(root.val)
#                 getResult(root.right, result)

#             return result

#         root = Node(intervals[0])
        
#         for interval in intervals[1:]:
#             tryAdd(root, interval)

#         return getResult(root)