#week07-2.py
#LeetCode 735
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            if a>0:
                ans.append(a)
            else:
                while ans and ans[-1]>0:
                    if abs(ans[-1]) == abs(a):
                        ans.pop()
                        a=0
                        break
                    elif abs(ans[-1]) > abs(a):
                        a = 0
                        break
                    else:
                        ans.pop()
                if a != 0: ans.append(a)
        return ans
