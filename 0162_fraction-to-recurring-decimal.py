class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
        numerator, denominator = abs(numerator), abs(denominator)
        integer = str(numerator // denominator)
        remainder = numerator % denominator

        remainder *= 10
        rmdset = []
        decimal = []
        while remainder > 0 and remainder not in rmdset:
            decimal.append(str(remainder // denominator))
            rmdset.append(remainder)
            remainder = remainder % denominator
            remainder *= 10
        if remainder > 0:
            loop_index = rmdset.index(remainder)
            ans = '{}{}.{}({})'.format(sign, integer, 
                ''.join(decimal[:loop_index]), ''.join(decimal[loop_index:]))
        elif len(decimal) > 0:
            ans ='{}{}.{}'.format(sign, integer, ''.join(decimal))
        else:
            ans = '{}{}'.format(sign, integer)
        return ans

if __name__ == '__main__':
    print(Solution().fractionToDecimal(1, 2))
    print(Solution().fractionToDecimal(2, 1))
    print(Solution().fractionToDecimal(2, 3))
    print(Solution().fractionToDecimal(4, 333))
    print(Solution().fractionToDecimal(1, 5))
    print(Solution().fractionToDecimal(7, 8))
    print(Solution().fractionToDecimal(8, 7))
    print(Solution().fractionToDecimal(1, 6))
