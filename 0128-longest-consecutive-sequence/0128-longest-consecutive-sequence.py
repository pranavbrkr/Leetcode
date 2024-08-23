class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()

        if not len(nums):
            return 0

        for number in nums:
            hash_set.add(number)
        
        print(hash_set)
        max_seq = 1

        for number in nums:
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