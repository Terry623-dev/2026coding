#week05-3.py
#LeetCode 1207
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        s = set()
        for c in counter:
            if counter[c] in s:
                return False
            s.add( counter[c] )
        return True
