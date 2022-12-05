class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        def containerSize(i, j):
            return min(height[i], height[j]) * (j - i)
        
        idx_1, idx_2 = 0, len(height)-1
        container = 0
        
        while idx_1 != idx_2:
            
            container = max(containerSize(idx_1, idx_2), container)
            
            if height[idx_1] > height[idx_2]:
                idx_2 -= 1
            else:
                idx_1 += 1
            
                    
        return container
            
            
                