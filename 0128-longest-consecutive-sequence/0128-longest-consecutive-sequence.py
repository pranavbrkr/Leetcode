class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_seq = 1
        num_set = set(nums)

        for num in num_set:
            if (num - 1) not in num_set:
                curr_seq = 1
                while (num + 1) in num_set:
                    num += 1
                    curr_seq += 1
                
                max_seq = max(max_seq, curr_seq)
        
        return max_seq