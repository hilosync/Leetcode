class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0

        charCount = {}
        result = 0
        while r < len(s):
            if s[r] in charCount:
                charCount[s[r]] += 1
            else:
                charCount[s[r]] = 1
            
            largestCount = max(charCount.values())

            if (r+1-l) - largestCount <= k:
                result = max(result, (r-l+1))
                r += 1
            else:
                charCount[s[l]] -= 1
                l += 1
                r += 1

        return result

