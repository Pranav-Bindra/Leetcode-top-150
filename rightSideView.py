# O(N)
# BFS on tree, first initialize a queue, append the root. while q is not empty, set qlen to len(q), then pop the first element q
# append to level. append left and right subtree to q. if level is not empty append to ans. Traverse res and add last element of every level to ans
# Beats 78.08%


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            level = []

            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                res.append(level)

        ans = []

        for i in range(len(res)):
            ans.append(res[i][-1])


        return ans