class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]

        primeNumbers = []
        i = 2
        while len(primeNumbers) < 26:
            isPrime = True
            for j in range(2,i):
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime:
                primeNumbers.append(i)
            i += 1
            
        def hashWord(word):
            hashedValue = 1
            for i in range(len(word)):
                hashedValue *= primeNumbers[ord(word[i])-ord('a')]
            return hashedValue

        wordDict = {}

        for word in strs:
            dictKey = hashWord(word)
            if dictKey in wordDict:
                wordDict[dictKey].append(word)
            else:
                wordDict[dictKey] = [word]
        
        return [x for x in wordDict.values()]

