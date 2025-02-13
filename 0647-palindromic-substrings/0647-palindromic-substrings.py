class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        n = len(s)

        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                answer += 1
        
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                answer += 1
        
        return answer