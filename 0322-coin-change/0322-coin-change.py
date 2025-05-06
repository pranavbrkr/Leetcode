class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(ret):
            if ret == 0:
                return 0
            if ret in cache:
                return cache[ret]
            
            res = amount + 1
            for c in coins:
                if (ret - c) >= 0:
                    res = min(res, 1 + dfs(ret - c))
            cache[ret] = res
            return res
        
        mincoins = dfs(amount)
        return -1 if mincoins == (amount + 1) else mincoins