#week12-3.py
# LeetCode 547. Number of Province
# matrix isConnected 裡，有些互相連 connected component?

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        path = defaultdict(list)

        for i in range(N):
            for j in range(N):
                if isConnected[i][j]:
                    path[i].append(j)
                    path[j].append(i)

        ans = 0
        visited = set()

        for i in range(N):
            if i in visited:
                continue

            visited.add(i)
            stack = [i]

            while stack:
                cur = stack.pop()

                for nxt in path[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        stack.append(nxt)

            ans += 1

        return ans
