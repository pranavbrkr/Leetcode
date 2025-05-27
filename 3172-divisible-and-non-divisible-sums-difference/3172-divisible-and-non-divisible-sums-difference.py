class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        non_div = 0
        div = 0

        for i in range(1, n + 1):
            non_div += i if i%m != 0 else 0
            div += i if i%m == 0 else 0
        
        return non_div - div