#week03-3.py
#LeetCode 1456
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = 0
        for i in range(k):
            if s[i] in vowels: count += 1
        ans = count
        N = len(s)
        for i in range(k, N):
            if s[i] in vowels: count += 1
            if s[i-k] in vowels: count -= 1
            ans = max(ans, count)
        return ans
