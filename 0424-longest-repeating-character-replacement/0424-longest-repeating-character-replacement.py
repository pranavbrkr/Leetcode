class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {}
        l = 0
        answer = 0

        for r in range(len(s)):
            char_map[s[r]] = 1 + char_map.get(s[r], 0)

            if (r - l + 1) - max(char_map.values()) > k:
                char_map[s[l]] -= 1
                l += 1
            
            answer = max(answer, r - l + 1)
        
        return answer

