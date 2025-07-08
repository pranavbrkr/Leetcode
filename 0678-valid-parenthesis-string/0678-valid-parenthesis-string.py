class Solution:
    def checkValidString(self, s: str) -> bool:
        minimum = 0
        maximum = 0

        for char in s:
            if char == "(":
                minimum += 1
                maximum += 1
            elif char == ")":
                minimum -= 1
                maximum -= 1
            else:
                minimum -= 1
                maximum += 1
            
            if minimum < 0:
                minimum = 0
            
            if maximum < 0:
                return False
        
        return (minimum == 0)