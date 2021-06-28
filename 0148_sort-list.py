# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if head is None:
            return None
        head, tail = self.merge_sort(head, None)
        return head

    def merge_sort(self, head, tail):
        # do not need to sort when it contains only one node
        if head.next is tail:
            return head, tail

        # find mid = slow      
        fast = slow = head
        while fast.next is not tail:
            fast = fast.next
            slow = slow.next
            if fast.next is tail:
                break
            else:
                fast = fast.next

        # merge sort left and right part
        lhead, ltail = self.merge_sort(head, slow)
        rhead, rtail = self.merge_sort(slow, tail)

        # merge
        hyperhead = pointer = ListNode()
        while lhead is not ltail or rhead is not rtail:
            if (lhead is not ltail and rhead is not rtail and lhead.val < rhead.val) \
                or (rhead is rtail):
                pointer.next = lhead
                pointer = lhead
                lhead = lhead.next
            else:
                pointer.next = rhead
                pointer = rhead
                rhead = rhead.next
        pointer.next = rtail

        return hyperhead.next, rtail

def initial_list(nums):
    head = pointer = ListNode(nums[0])
    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        pointer.next = node
        pointer = node
    return head

def output_head(head):
    ans = []
    while head is not None:
        ans.append(head.val)
        head = head.next
    return ans

if __name__ == '__main__':
    head = initial_list([4,2,1,3])
    print(output_head(head))
    head = Solution().sortList(head)
    print(output_head(head))

    head = initial_list([-1,5,3,4,0])
    print(output_head(head))
    head = Solution().sortList(head)
    print(output_head(head))