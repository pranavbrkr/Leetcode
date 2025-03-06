class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        count_t, window = defaultdict(int), defaultdict(int)

        for c in t:
            count_t[c] += 1

        have, need = 0, len(count_t)
        answer, answer_len = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < answer_len:
                    answer = [l, r]
                    answer_len = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
            
        l, r = answer
        return s[l : r + 1] if answer != float("inf") else ""