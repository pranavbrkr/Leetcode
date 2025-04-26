class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr_set = set()

        for number in nums:
            if number in arr_set:
                return True
            arr_set.add(number)

        return False