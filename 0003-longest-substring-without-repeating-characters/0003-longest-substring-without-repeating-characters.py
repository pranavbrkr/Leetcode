class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charmap = {}
        answer = 0
        l = 0

        for r in range(len(s)):
            if s[r] in charmap:
                l = max(charmap[s[r]] + 1, l)
            charmap[s[r]] = r
            answer = max(answer, r - l + 1)
        
        return answer