class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s_len = len(s)
        g_len = len(g)

        g.sort()
        s.sort()

        l, r = 0, 0

        while l < s_len:
            if r == g_len:
                return g_len
            if g[r] <= s[l]:
                r += 1
            l += 1
        
        return r