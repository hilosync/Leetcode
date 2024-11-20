class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]

        totalWater = 0

        while l < r:
            if maxLeft <= maxRight:
                totalWater += maxLeft-height[l]
                l += 1
                maxLeft = max(maxLeft, height[l])
            
            else:
                totalWater += maxRight-height[r]
                r -= 1
                maxRight = max(maxRight, height[r])

        return totalWater



            