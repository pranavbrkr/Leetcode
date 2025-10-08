class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        hay_len = len(haystack)

        for i in range(hay_len - needle_len + 1):
            if needle == haystack[i : i + needle_len]:
                return i
        
        return -1