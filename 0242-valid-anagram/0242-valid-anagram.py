class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = [0] * 26

        for i, ch in enumerate(s):
            counter[ord(ch) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
        
        for cnt in counter:
            if cnt != 0:
                return False
        
        return True