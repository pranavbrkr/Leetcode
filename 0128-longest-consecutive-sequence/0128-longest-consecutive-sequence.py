class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        max_seq = 1

        for number in num_set:
            if (number - 1) not in num_set:
                curr_seq = 1
                while (number + 1) in num_set:
                    curr_seq += 1
                    number += 1
                
                max_seq = max(max_seq, curr_seq)
        
        return max_seq