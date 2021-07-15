# https://leetcode.com/problems/balanced-binary-tree/

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Helped solution from discussions.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        self.balance = True
        self.check(root)
        return self.balance
        
    def check(self, node:TreeNode):
        
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1

        left = self.check(node.left)
        right = self.check(node.right)
        
        if abs(left - right) > 1:
            self.balance = False
            
        return max(left,right) + 1

def test_balanced_tree():
    solution = Solution()
    root = TreeNode(3,TreeNode(9),TreeNode(20, TreeNode(15), TreeNode(7)))
    print(solution.isBalanced(root))
    root2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    print(solution.isBalanced(root2))

if __name__ == '__main__':
    test_balanced_tree()