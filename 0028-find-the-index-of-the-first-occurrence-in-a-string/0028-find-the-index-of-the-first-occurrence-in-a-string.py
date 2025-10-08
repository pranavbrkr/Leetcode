class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        hay_len = len(haystack)
        needle_index = 0

        for i in range(hay_len - needle_len + 1):
            if needle[needle_index] == haystack[i]:
                if needle[needle_index : needle_index + needle_len] == haystack[i : i + needle_len]:
                    return i
        
        return -1