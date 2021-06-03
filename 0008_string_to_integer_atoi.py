# status: Pre Sgn Num End
#           PRE     SGN     NUM     END
#   PRE       =     +/-    [0-9]  other
#   SGN       /       0    [1-9]  other
#   NUM       /       /    [0-9]  other
#   END       /       /        /      /

# sign          +/-
# space         =
# number        [0-9]

class Solution:
    def myAtoi(self, s):
        digits = list('0123456789')
        maxn = '2147483648'
        status = 'PRE'
        sign = False
        numbers = []

        for c in s:
            if status == 'PRE':
                if c == ' ':
                    continue
                elif c == '-' or c == '+':
                    sign = (c == '-')
                    status = 'SGN'
                    continue
                elif c == '0':
                    status = 'SGN'
                    continue
                elif c in digits:
                    status = 'NUM'
                    numbers.append(c)
                    continue
                else:
                    break
            elif status == 'SGN':
                if c == '0':
                    continue
                elif c in digits:
                    status = 'NUM'
                    numbers.append(c)
                    continue
                else:
                    break
            elif status == 'NUM':
                if c in digits:
                    numbers.append(c)
                else:
                    break

        if len(numbers):
            if sign:
                if len(numbers) > 10:
                    return -2147483648
                else:
                    return max(int('-' + ''.join(numbers)), -2147483648)
            else:
                if len(numbers) > 10:
                    return 2147483647
                else:
                    return min(int(''.join(numbers)), 2147483647)
        else:
            return 0




