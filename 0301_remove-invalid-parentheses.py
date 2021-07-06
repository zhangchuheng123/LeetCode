import pdb

class Solution:
    def is_valid(self, str_list):
        count = 0
        for c in str_list:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                return False
        if count == 0:
            return True
        else:
            return False

    def removeInvalidParentheses(self, s):
        s = list(s)

        do_find_answer = False
        ans = []
        queue = [s]
        tmp_queue = []
        while len(queue) > 0 or ((not do_find_answer) and len(tmp_queue) > 0):
            if len(queue) == 0:
                tmp_queue = list(set(tmp_queue))
                queue = [list(item) for item in tmp_queue]
            str_list = queue.pop(0)
            if self.is_valid(str_list):
                do_find_answer = True
                ans.append(''.join(str_list))
            if not do_find_answer:
                for i, c in enumerate(str_list):
                    if c in ['(', ')']:
                        str_copy = str_list.copy()
                        str_copy.pop(i)
                        tmp_queue.append(''.join(str_copy))

        return list(set(ans))

if __name__ == '__main__':
    print(Solution().removeInvalidParentheses(")(((((((("))
    print(Solution().removeInvalidParentheses("((()((s((((()"))