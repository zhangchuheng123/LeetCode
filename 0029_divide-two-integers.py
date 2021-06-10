# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 返回被除数 dividend 除以除数 divisor 得到的商。
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

# 示例 1:
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

# 示例 2:
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2

# 提示：

# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31, 2^31−1]。本题中，如果除法结果溢出，则返回 2^31− 1。

MAXN = 2147483647
MINN = -2147483648

class Solution:
    def divide(self, dividend, divisor):

        if dividend == 0:
            return 0
        elif divisor == 1:
            return dividend
        elif divisor == -1:
            if dividend == MINN:
                return MAXN
            else:
                return -dividend

        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)

        def div(x, y):
            if x < y:
                return 0
            elif x == y:
                return 1

            ans = 1
            prod = y
            while (x >= prod + prod):
                prod += prod
                ans += ans
            return ans + div(x - prod, y)

        return sign * div(dividend, divisor)

if __name__ == '__main__':
    print(Solution().divide(10, 3))
    print(Solution().divide(7, -3))
    print(Solution().divide(0, 5))
    print(Solution().divide(2147483647, -1))
    print(Solution().divide(-2147483648, -1))
    print(Solution().divide(2048, 2))
    print(Solution().divide(2051, 2))