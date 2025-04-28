class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charmap = {}
        l = 0
        answer = 0

        for r in range(len(s)):
            charmap[s[r]] = 1 + charmap.get(s[r], 0)

            if (r - l + 1) - max(charmap.values()) > k:
                charmap[s[l]] -= 1
                l += 1
            
            answer = max(answer, r - l + 1)
        
        return answer