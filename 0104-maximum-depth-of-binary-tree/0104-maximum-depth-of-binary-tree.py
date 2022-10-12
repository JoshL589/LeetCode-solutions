# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.result = 0
        self.count = 1
        self.preorder(root)
        return self.result
        
    def preorder(self, current):
        self.result = max(self.count, self.result)
        if current.left:
            self.count += 1
            self.preorder(current.left)
            
        if current.right:
            self.count += 1
            self.preorder(current.right)
            
        self.count -= 1