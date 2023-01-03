class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced(node: Optional[TreeNode]) -> bool:
            # base case: empty tree is balanced
            if not node:
                return True, 0
            
            # check if left subtree is balanced
            left_balanced, left_height = is_balanced(node.left)
            if not left_balanced:
                return False, 0
            
            # check if right subtree is balanced
            right_balanced, right_height = is_balanced(node.right)
            if not right_balanced:
                return False, 0
            
            # check if current tree is balanced
            if abs(left_height - right_height) > 1:
                return False, 0
            
            # tree is balanced, return height
            return True, max(left_height, right_height) + 1

        return is_balanced(root)[0]
