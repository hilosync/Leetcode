class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dpSolutions = [False] * (len(s)+1)
        dpSolutions[len(s)] = True

        for i in range(len(s)-1, -1 ,-1):
            for word in wordDict:
                if i+len(word) <= len(s) and s[i:i+len(word)] == word:
                    dpSolutions[i] = dpSolutions[i+len(word)]
                if dpSolutions[i]:
                    break

        return dpSolutions[0]
