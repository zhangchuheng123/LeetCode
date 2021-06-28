class Solution:

    @staticmethod
    def word2subword(word):
        ans = []
        for i in range(len(word)):
            tmp = list(word)
            tmp[i] = '*'
            ans.append(''.join(tmp))
        return ans

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        full_list = [beginWord] + wordList
        conn_dict = dict()

        for word in full_list:
            subwords = self.word2subword(word)
            conn_dict[word] = subwords
            for subword in subwords:
                if subword in conn_dict:
                    conn_dict[subword].append(word)
                else:
                    conn_dict[subword] = [word]

        # dist can be optimized: use a list instead of dict
        dist = {beginWord: 2}
        queue = [beginWord]
        while len(queue) > 0:
            word = queue.pop(0)
            for toword in conn_dict[word]:
                if toword == endWord:
                    return (dist[word] + 1) // 2
                if toword not in dist:
                    dist[toword] = dist[word] + 1
                    queue.append(toword)
        return 0

