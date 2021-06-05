DICT = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}
EMPTY = ['']

class Solution:
    def letterCombinations(self, digits):

        ans = []
        n = len(digits)
        
        if n == 0:
            return []
        # Pay attention to this boundary condition

        a1 = DICT[digits[0]] if n > 0 else EMPTY
        a2 = DICT[digits[1]] if n > 1 else EMPTY
        a3 = DICT[digits[2]] if n > 2 else EMPTY
        a4 = DICT[digits[3]] if n > 3 else EMPTY

        for c1 in a1:
            for c2 in a2:
                for c3 in a3:
                    for c4 in a4:
                        ans.append(''.join([c1, c2, c3, c4]))

        return ans 
        