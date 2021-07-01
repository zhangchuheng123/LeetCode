# Pay attention to the numerical error in calculation
from math import sqrt

c1 = (3 + sqrt(5)) / 2 / sqrt(5)
c2 = (3 - sqrt(5)) / 2 / sqrt(5)
l1 = (1 + sqrt(5)) / 2
l2 = (1 - sqrt(5)) / 2

class Solution:
    def climbStairs(self, n):
        return round(c1 * l1 ** (n - 1) - c2 * l2 ** (n - 1))
