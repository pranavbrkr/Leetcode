class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        hash_set = set(nums)

        max_seq = 1

        for number in hash_set:
            if number - 1 in hash_set:
                continue
            else:
                curr_seq = 1
                while number + 1 in hash_set:
                    curr_seq += 1
                    number += 1
                
                if max_seq < curr_seq:
                    max_seq = curr_seq

        return max_seq