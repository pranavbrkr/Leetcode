class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        answer = 0

        def countPalindromes(l, r):
            num_pal = 0
            while l >= 0 and r < n and s[l] == s[r]:
                num_pal += 1
                l -= 1
                r += 1
            return num_pal
        
        for i in range(n):
            answer += countPalindromes(i, i)
            answer += countPalindromes(i, i + 1)
        
        return answer