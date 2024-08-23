import re
import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        numbers = re.findall(r'[+-]?\d+/\d+', expression)
        numerators = []
        denominators = []

        for number in numbers:
            numerators.append(int(number[:number.find('/')]))
            denominators.append(int(number[number.find('/') + 1:]))

        lcm = math.lcm(*denominators)
        for i, num in enumerate(numerators):
            numerators[i] = numerators[i] * (lcm // denominators[i])

        summation = sum(numerators)

        gcd = math.gcd(summation, lcm)

        ans_num = summation // gcd
        ans_den = lcm // gcd

        return str(ans_num) + "/" + str(ans_den)