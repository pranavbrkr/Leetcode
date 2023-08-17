# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict = dict()
        nums_len = len(nums)
        ret_list = []

        for i in range(nums_len):
            mydict[nums[i]] = i
        
        for i in range(nums_len):
            pair_index = mydict.get(target - nums[i])
            if pair_index is not None and pair_index != i:
                ret_list.append(i)
                ret_list.append(pair_index)
                break

        return ret_list