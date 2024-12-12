import math
import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapq.heapify(gifts)

        for i in range(k):
            currPile = -heapq.heappop(gifts)
            newPile = math.floor(sqrt(currPile))
            heapq.heappush(gifts, -newPile)
        
        return -sum(gifts)

