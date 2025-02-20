class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        if not s:
            return 0

        sign = 1
        result = 0

        if s[0] in "-+":
            sign = -1 if s[0] == "-" else 1
            s = s[1:]
        
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
        
        result = result * sign

        if result > (2**31 - 1):
            return (2**31 - 1)
        elif result < -2**31:
            return -2**31

        return result