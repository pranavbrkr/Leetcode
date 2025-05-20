class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) -1, -1 ,-1):
            if carry:
                carry = carry + digits[i]
                print(carry)
                digits[i] = carry % 10
                print(digits[i])
                carry = carry // 10
                print(carry)
        
        if carry != 0:
            return[carry] + digits
        else:
            return digits