# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList):
        self.queue = []
        self.ind = 0
        self.dfs(nestedList)

    def dfs(self, nested_list):
        for item in nested_list:
            if item.isInteger():
                self.queue.append(item.getInteger())
            else:
                self.dfs(item.getList())
    
    def next(self):
        ans = self.queue[self.ind]
        self.ind += 1
        return ans
    
    def hasNext(self):
        return self.ind < len(self.queue)
         

if __name__ == '__main__':
    nestedList = [[1,1],2,[1,1]]
    # Your NestedIterator object will be instantiated and called as such:
    i, v = NestedIterator(nestedList), []
    while i.hasNext(): 
        v.append(i.next())
    print(v)