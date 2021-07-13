# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

# 示例 :
# 给定二叉树

#           1
#          / \
#         2   3
#        / \     
#       4   5    
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

# 注意：两结点之间的路径长度是以它们之间边的数目表示。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        num_nodes, _ = self.search(root)
        return num_nodes - 1

    def search(self, node):
        if node is None:
            return 0, 0
        num_nodes_l, num_nodes_inc_l = self.search(node.left)
        num_nodes_r, num_nodes_inc_r = self.search(node.right)
        num_nodes_inc = max(num_nodes_inc_l, num_nodes_inc_r) + 1
        num_nodes = max(num_nodes_l, num_nodes_r, num_nodes_inc_r + num_nodes_inc_l + 1)

        return num_nodes, num_nodes_inc