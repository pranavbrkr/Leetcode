
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)

        for s in s1:
            s1_count[s] += 1

        for s in s2[:m]:
            s2_count[s] += 1

        start = 0
        end = m - 1

        matches = 0
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        
        for alphabet in alphabets:
            if s1_count[alphabet] == s2_count[alphabet]:
                matches += 1

        if matches == 26:
            return True
        
        s2_count[s2[start]] -= 1
        start +=1
        end += 1


        while end < n:
            s2_count[s2[end]] += 1
            matches = 0
            for alphabet in alphabets:
                if s1_count[alphabet] == s2_count[alphabet]:
                    matches += 1
            
            if matches == 26:
                return True
            
            s2_count[s2[start]] -= 1
            start +=1
            end += 1

        return False