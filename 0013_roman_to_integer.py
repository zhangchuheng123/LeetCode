class Solution:
    def romanToInt(self, s):
        p = 0
        end = len(s)
        num = 0

        single = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        double = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        
        while p < end:
            if (p + 1 < end) and (s[p:p+2] in double.keys()):
                num += double[s[p:p+2]]
                p += 2
            else:
                num += single[s[p]]
                p += 1
                
        return num


