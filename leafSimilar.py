# First Approach :- O(N)
# if root.left and root.right is none, append to leaves. Call function on left and right subtree until reaches none. Call function on root1 and root2, return both lists
# Beats 60.53%



class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafValues(root, leaves):
            if not root:
                return
            
            if not root.left and not root.right:
                leaves.append(root.val)
                return 
            
            getLeafValues(root.left, leaves)
            getLeafValues(root.right, leaves)

        leaf_vals1 = []
        leaf_vals2 = []

        getLeafValues(root1, leaf_vals1)
        getLeafValues(root2, leaf_vals2)

        return leaf_vals1 == leaf_vals2