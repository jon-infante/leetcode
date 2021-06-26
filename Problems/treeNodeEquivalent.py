# Definition for a binary tree node.



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # if either is None, both has to be None
        if not p or not q:
            return (p is None) and (q is None)
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        


if __name__ == '__main__':
    p = TreeNode(1,2,3)
    q = TreeNode(1,2,3)
    solution=Solution()
    print(solution.isSameTree(p,q))
