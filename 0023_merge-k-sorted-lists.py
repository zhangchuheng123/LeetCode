# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6

class Solution:
    def mergeKLists(self, lists):

        if len(lists) == 0:
            return None

        lists = [l for l in lists if l is not None]
        lists = sorted(lists, key=lambda x: x.val)

        head = tail = None

        while len(lists):

            tmp = lists.pop(0)

            if head is None:
                head = tail = tmp
                tmp = tmp.next
            else:
                tail.next = tmp
                tail = tail.next
                tmp = tmp.next

            # Pay attention to the conditions here
            # We can use binary search for a O(n logn) algorithm
            if tmp is not None:
                i = 0
                while len(lists) > 0 and i < len(lists) and lists[i].val < tmp.val:
                    i += 1
                lists.insert(i, tmp)

        return head
