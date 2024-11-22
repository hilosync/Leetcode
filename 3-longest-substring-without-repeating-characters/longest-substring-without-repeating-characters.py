class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l,r = 0, 0
        maxSubstring = 0
        newSet = set()
        currSubstring = 0

        while r < len(s):
        
            while r < len(s) and s[r] not in newSet:
                newSet.add(s[r])
                currSubstring += 1
                maxSubstring = max(maxSubstring, currSubstring)
                r += 1
            
            if r < len(s):
                while l < r and s[l] != s[r]:
                    currSubstring -= 1
                    newSet.remove(s[l])
                    l += 1
                l += 1
                r += 1

        return maxSubstring



