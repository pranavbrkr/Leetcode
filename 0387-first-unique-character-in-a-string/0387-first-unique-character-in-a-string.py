class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = defaultdict(int)

        for c in s:
            char_map[c] += 1
        
        for i, c in enumerate(s):
            if char_map[c] == 1:
                return i
        
        return -1