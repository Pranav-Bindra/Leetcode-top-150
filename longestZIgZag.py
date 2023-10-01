# O(N)
# Create helper function, 3 arguments, node, isLeft(boolean) to keep track of the last move, depth to keep track of depth, if last move was left, recursiovely go right, if there you can go there 
# or else update the depth to 1 and go left.
# Beats 94.17%


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self.helper(root.left, True, 0),self.helper(root.right, False, 0))  

    def helper(self, node, isLeft, depth):
        if not node:
            return depth

        if isLeft:
            depth = max(depth,
            self.helper(node.right, False, depth+1),
            self.helper(node.left, True, 0))
                
        else:
            depth = max(depth,
            self.helper(node.left, True, depth+1),
            self.helper(node.right, False, 0))

        return depth 