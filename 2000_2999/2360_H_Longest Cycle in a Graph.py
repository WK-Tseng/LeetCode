class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        
        result = -1
        visit = set()
        for i in range(n):
            if i not in visit:
                stack = []
                p = i
                while p != -1 and p not in visit:
                    visit.add(p)
                    stack.append(p)
                    p = edges[p]
                
                count = -1
                for idx, d in enumerate(stack[::-1]):
                    if d == p:
                        count = idx + 1
                        result = max(result, count)
                        break
        return result