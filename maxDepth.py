# First Approach :- O(N)
# Base case, if none retun 0, recursively call the maximum from the left or the right subtree
# Beats 70.71%


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            leftmax = self.maxDepth(root.left)
            rightmax = self.maxDepth(root.right)
        
        return 1+ max(leftmax,rightmax)