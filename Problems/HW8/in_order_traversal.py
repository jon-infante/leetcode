#Given a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recurse(self, root, vals):
        """Time Complexity: O(n)"""
        if(root == None):
            return

        self.rec(root.left, vals)
        vals.append(root.val)
        self.rec(root.right, vals)

    def inorderTraversal(self, root):
        vals = []
        self.rec(root, vals)
        return vals