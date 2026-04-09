#week07-6.py
#LeetCode 649
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))
        banR, banD = 0, 0
        R = senate.count('R')  # 初始化
        D = senate.count('D')

        while R > 0 and D > 0:  # 防止死循環
            now = queue.popleft()

            if now == 'R':
                if banR > 0:
                    banR -= 1
                    R -= 1
                else:
                    banD += 1
                    queue.append(now)
            else:  # 'D'
                if banD > 0:
                    banD -= 1
                    D -= 1
                else:
                    banR += 1
                    queue.append(now)

        if R == 0:
            return 'Dire'
        if D == 0:
            return 'Radiant'
