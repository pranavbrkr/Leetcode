class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0

        for number in nums:
            xor = xor ^ number
        
        return xor