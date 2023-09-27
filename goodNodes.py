# O(N)
# DFS, return res, check if node.val>=current max val for that subtree
# Beats 81.33%


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def routes(root,maxVal):
            if not root:
                return 0
            
            if root.val>=maxVal:
                res=1
            else:
                res = 0

            maxVal = max(root.val,maxVal)

            res += routes(root.left,maxVal)
            res += routes(root.right,maxVal)


            return res
        
        return routes(root,root.val)
