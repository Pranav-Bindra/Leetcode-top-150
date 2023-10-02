# O(N) 
# if any match is there return Node, else return None. Traverse the subtree dfs. If both left and right are returning something, return node else return whichever is not null
# Beats 84.13%


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        else:
            return left or right

        
