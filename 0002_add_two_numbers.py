# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2, jw=0):
        if l1 is not None and l2 is not None:
            tot = l1.val + l2.val + jw
            n1 = l1.next
            n2 = l2.next
            flag = True
        elif l1 is None and l2 is not None:
            tot = l2.val + jw
            n1 = None
            n2 = l2.next
            flag = True
        elif l1 is not None and l2 is None:
            tot = l1.val + jw
            n1 = l1.next
            n2 = None
            flag = True
        elif l1 is None and l2 is None and jw != 0:
            n1 = None
            n2 = None
            tot = jw
            flag = True
        else:
            flag = False