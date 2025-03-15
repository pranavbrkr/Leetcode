class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charmap = {}
        max_len = 0
        l = 0

        for r in range(len(s)):
            if s[r] in charmap:
                l = max(charmap[s[r]] + 1, l)
            charmap[s[r]] = r
            max_len = max(max_len, r - l + 1)
        
        return max_len