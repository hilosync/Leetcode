class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        l, r = 0, 1
        rightMax = height[r]

        totalWater = 0
        def findMax(rightPointer):
            index = rightPointer
            currMax = 0
            for i in range(rightPointer+1, len(height)):
                if height[i] >= currMax:
                    currMax = height[i]
                    index = i
            
            return index



        for i in range(1,len(height)-1):
            
            if i == r:
                r = findMax(r)
            
            currentWater = min(height[l], height[r]) - height[i]

            if currentWater > 0:
                totalWater += currentWater
        
            if height[i] > height[l]:
                l = i

        return totalWater
            