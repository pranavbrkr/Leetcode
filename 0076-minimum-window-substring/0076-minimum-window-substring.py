class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countt, window = defaultdict(int), defaultdict(int)

        for char in t:
            countt[char] += 1

        answer = [-1, -1]
        answer_len = float('inf')
        have, need = 0, len(countt)

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in countt and window[c] == countt[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < answer_len:
                    answer = [l, r]
                    answer_len = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countt and window[s[l]] < countt[s[l]]:
                    have -= 1
                l += 1
        
        l, r = answer
        
        return s[l:r + 1] if answer_len != float("inf") else ""