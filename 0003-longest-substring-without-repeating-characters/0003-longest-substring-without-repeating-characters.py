class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        answer = 0
        l = 0

        for r in range(len(s)):
            if s[r] in char_map:
                l = max(char_map[s[r]] + 1, l)
            char_map[s[r]] = r
            answer = max(answer, r - l + 1)
        
        return answer