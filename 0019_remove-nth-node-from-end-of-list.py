# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        node_list = []
        while head:
            node_list.append(head)
            head = head.next

        num_nodes = len(node_list)
        last_n_ind = num_nodes - n
        if last_n_ind >= 1:
            node_list[last_n_ind - 1].next = node_list[last_n_ind].next
            return node_list[0]
        else:
            return node_list[0].next 
