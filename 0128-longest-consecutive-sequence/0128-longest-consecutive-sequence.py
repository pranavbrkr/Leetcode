class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_seq = 1
        num_set = set(nums)

        for number in num_set:
            if (number - 1) not in num_set:
                length = 1

                while (length + number) in num_set:
                    length += 1
                
                max_seq = max(max_seq, length)
        
        return max_seq