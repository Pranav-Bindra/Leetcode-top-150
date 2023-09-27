# O(N)
# basic dfs function calling a helper function to check the downward sum from that particular node
# Beats 12.72%

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        def helper(node,curr):
            if not node:
                return None
            
            helper(node.left, curr+node.val)
            helper(node.right, curr+node.val)

            if curr + node.val == targetSum:
                self.res+=1
        
        def dfs(node):
            if not node:
                return None
            
            helper(node,0)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.res