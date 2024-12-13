class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        pathsDict = {x:[] for x in range(1,n+1)}
        for path in paths:
            pathsDict[path[0]].append(path[1])
            pathsDict[path[1]].append(path[0])

        notVisited = set(x for x in range(1,n+1))
        toVisit = [1]

        possiblePaints = {x:[1,2,3,4] for x in range(1,n+1)}
        results = [0]*n
        while notVisited:
            if not toVisit:
                currGarden = notVisited.pop()
            else:
                currGarden = toVisit.pop()
                if currGarden in notVisited:
                    notVisited.remove(currGarden)
            flower = possiblePaints[currGarden][0]
            results[currGarden-1] = flower

            for neighbour in pathsDict[currGarden]:
                if neighbour in notVisited:
                    if flower in possiblePaints[neighbour]:
                        possiblePaints[neighbour].remove(flower)
                    toVisit.append(neighbour)
        
        return results
            

            



