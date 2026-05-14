# week12-4.py 學習圖 Graph - DFS 第3題，還是 Medium 呢
# LeetCode 1466. Reorder Routes to Make All Paths Lead to the City Zero --- 之後，有空再寫
# 有 N 個城市，有 N-1 條路，希望大家走到 0 都是正向，有幾條會「錯掉」?
# 解法: 從 0 出發，全部走過，路不對，就 ans += 1

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()  # 走過的，不要再走
        path = defaultdict(list)  # path[now] 與哪些 city 相接

        for a, b in connections:
            path[a].append((b, +1))
            path[b].append((a, -1))

        # print(path[1])

        def helper(now):
            ans = 0  # 有幾條路「方向不對」
            visited.add(now)

            for k, d in path[now]:  # 城市 now 可以到城市 k，方向是 d
                if k not in visited:
                    if d == +1:
                        ans += 1  # 要換個方向，若方向「錯掉」
                    ans += helper(k)  # 往前呼叫遞迴，理由會繼續「出錯」

            return ans

        return helper(0)  # 從 0 出發
