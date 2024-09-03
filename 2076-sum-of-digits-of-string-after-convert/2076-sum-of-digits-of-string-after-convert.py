class Solution:
    def getLucky(self, s: str, k: int) -> int:
        char_str = ""
        for char in s:
            char_str += str(ord(char) - 96)


        while k:
            char_sum = sum([int(char) for char in char_str])
            char_str = str(char_sum)
            k -= 1

        return int(char_str)