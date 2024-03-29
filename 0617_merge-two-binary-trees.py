# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

# 示例 1:

# 输入: 
#     Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# 输出: 
# 合并后的树:
#          3
#         / \
#        4   5
#       / \   \ 
#      5   4   7
# 注意: 合并必须从两个树的根节点开始。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        new_root = self.createNode(root1, root2)
        return new_root

    def createNode(self, node1, node2):
        if node1 is None and node2 is None:
            return None

        if node1 is not None:
            val1 = node1.val
            left1 = node1.left
            right1 = node1.right
        else:
            val1 = 0
            left1 = None
            right1 = None

        if node2 is not None:
            val2 = node2.val
            left2 = node2.left
            right2 = node2.right
        else:
            val2 = 0
            left2 = None
            right2 = None
            
        return TreeNode(val1 + val2, self.createNode(left1, left2), self.createNode(right1, right2))