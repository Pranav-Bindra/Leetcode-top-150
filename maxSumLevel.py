# O(N)
# BFS on tree, for loop for appending sum at each level, Return index at max_sum
# Beats 50.63%


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        q = collections.deque()
        q.append(root)

        res = []

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
        
        tracker = []

        for i in range(len(res)):
            tracker.append(sum(res[i]))

        max_sum = max(tracker)

        return (tracker.index(max_sum))+1