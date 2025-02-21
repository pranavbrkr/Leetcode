class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        answer = 0
        n = len(s)

        while i < n:
            if s[i] == "M":
                answer += 1000
                i += 1
            elif s[i] == "D":
                answer += 500
                i += 1 
            elif s[i] == 'L':
                answer += 50
                i += 1
            elif s[i] == 'V':
                answer += 5
                i += 1
            elif s[i] == 'C':
                if i < n - 1 and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                    if s[i + 1] == 'D':
                        answer += 400
                    elif s[i + 1] == 'M':
                        answer += 900
                    i += 2
                else:
                    answer += 100
                    i += 1
            elif s[i] == 'X':
                if i < n - 1 and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    if s[i + 1] == 'L':
                        answer += 40
                    elif s[i + 1] == 'C':
                        answer += 90
                    i += 2
                else:
                    answer += 10
                    i += 1
            elif s[i] == 'I':
                if i < n - 1 and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    if s[i + 1] == 'V':
                        answer += 4
                    elif s[i + 1] == 'X':
                        answer += 9
                    i += 2
                else:
                    answer += 1
                    i += 1
        
        return answer