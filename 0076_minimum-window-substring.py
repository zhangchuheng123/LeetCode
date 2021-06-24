class Solution:
    def minWindow(self, s, t):
        lens = len(s)
        minlen = 100001
        minstr = ''
        # first: count in the window, second: count in t
        record = {c: [0, 0] for c in list(set(list(t)))}
        for c in t:
            record[c][1] += 1

        def all_filled(record):
            for val in record.values():
                if val[0] < val[1]:
                    return False
            return True

        indlist = [i for i, c in enumerate(s) if c in record]
        
        ii = 0
        for j in indlist:
            if s[j] in record:
                record[s[j]][0] += 1
            if all_filled(record):
                while record[s[indlist[ii]]][0] > record[s[indlist[ii]]][1]:
                    record[s[indlist[ii]]][0] -= 1
                    ii += 1
                curr_len = j - indlist[ii] + 1
                if minlen > curr_len:
                    minlen = curr_len
                    minstr = s[indlist[ii]:j+1]

        return minstr
