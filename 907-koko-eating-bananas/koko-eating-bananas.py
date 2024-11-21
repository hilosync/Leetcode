import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = l + ((r-l)//2)

            eatingTime = 0
            for pile in piles:
                eatingTime += math.ceil(pile/mid)
                
            if eatingTime > h:
                l = mid + 1
            else:
                r = mid - 1
        
        return l





                



        

