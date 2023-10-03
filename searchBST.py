# O(log(n))
# if end of tree: return None, if value equal return True, if value is greater, traverse left else traverse right
# Beats 12.64%



class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val>val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right,val)