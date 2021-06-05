# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = node = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, remain = divmod(v1 + v2 + carry, 10)
            tmp = ListNode(remain)
            node.next = tmp
            node = node.next
        return root.next


def construct_listnode(x):
    root = node = ListNode(0)
    for i in x:
        tmp = ListNode(i)
        node.next = tmp
        node = node.next
    return root.next


def print_listnode(x):
    s = ''
    while x:
        if s:
            s += ' -> '
        s += str(x.val)
        x = x.next
    print(s)

if __name__ == '__main__':
    l1 = construct_listnode([2, 4, 3])
    l2 = construct_listnode([5, 6, 4])
    solution = Solution()
    ans = solution.addTwoNumbers(l1, l2)
    print_listnode(ans)
