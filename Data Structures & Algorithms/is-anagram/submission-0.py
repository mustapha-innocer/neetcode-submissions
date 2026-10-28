from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_count = Counter(s)
        t_count = Counter(t)

        if len(s_count.keys()) != len(t_count.keys()):
            return False

        for k, v in s_count.items():
            if t_count.get(k) is None or t_count.get(k) != v:
                return False
        
        return True
