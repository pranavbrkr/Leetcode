class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindromes(left, right):
            answer = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                answer += 1
                left -= 1
                right += 1
            return answer
        
        result = 0
        for i in range(len(s)):
            result += countPalindromes(i, i)
            result += countPalindromes(i, i + 1)

        return result