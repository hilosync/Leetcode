class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        playerDict = {}

        for winner, loser in matches:
            if winner not in playerDict:
                playerDict[winner] = 0
            
            if loser not in playerDict:
                playerDict[loser] = 1
            else:
                playerDict[loser] += 1
        
        results = [[],[]]

        for key, value in playerDict.items():
            if value == 0:
                results[0].append(key)
            if value == 1:
                results[1].append(key)
        
        results[0].sort()
        results[1].sort()
        return results


