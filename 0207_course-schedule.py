class Solution:
    def canFinish(self, numCourses, prerequisites):
        full_list = [p[0] for p in prerequisites] + [p[1] for p in prerequisites]
        full_dict = dict()
        for p in prerequisites:
            if p[0] in full_dict:
                full_dict[p[0]].append(p[1])
            else:
                full_dict[p[0]] = [p[1]]

        full_set = set(full_list)
        visited = full_set - set([p[0] for p in prerequisites])
        tmp = [0]
        while len(tmp) > 0:
            tmp = []
            for key, val in full_dict.items():
                full_dict[key] = [v for v in val if v not in visited]
                if len(full_dict[key]) == 0:
                    tmp.append(key)
            for key in tmp:
                del full_dict[key]
                visited.add(key)
        if visited == full_set:
            return True
        else:
            return False

if __name__ == '__main__':
    print(Solution().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))