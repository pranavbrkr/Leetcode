class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        answer = 0

        for i in range(len(s)):
            if (i + 1) < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                answer -= roman_map[s[i]]
            else:
                answer += roman_map[s[i]]

        return answer