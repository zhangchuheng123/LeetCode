# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):

        head = None
        tail = None

        while l1 or l2:
            if (l1 and l2 and l1.val < l2.val) or (l2 is None):
                if head:
                    tail.next = l1
                    tail = l1
                else:
                    head = tail = l1
                l1 = l1.next
            else:
                if head:
                    tail.next = l2
                    tail = l2
                else:
                    head = tail = l2
                l2 = l2.next

        return head

