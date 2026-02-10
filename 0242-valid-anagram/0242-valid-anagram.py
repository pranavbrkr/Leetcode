class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_map = defaultdict(int)

        for c in s:
            char_map[c] += 1
        
        for c in t:
            char_map[c] -= 1
        
        for k, v in char_map.items():
            if v:
                return False
        
        return True