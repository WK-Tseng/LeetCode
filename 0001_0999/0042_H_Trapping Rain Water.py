class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        leftH, rightH = height[left], height[right]
        water = 0
        while left <= right:
            if height[left] > leftH:
                leftH = height[left]
            if height[right] > rightH:
                rightH = height[right]

            if leftH <= rightH:
                water += leftH - height[left]
                left += 1
            else:
                water += rightH - height[right]
                right -= 1
        return water