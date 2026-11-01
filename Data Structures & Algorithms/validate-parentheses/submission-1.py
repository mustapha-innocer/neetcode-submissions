class Solution:
    def isValid(self, s: str) -> bool:
        bkts = {
            ']': '[', '}': '{', ')': '('
        }
        stack = []
        for ch in s:
            if ch not in bkts.keys():
                stack.append(ch)
            elif len(stack) == 0 or ch in bkts and stack.pop() != bkts[ch]:
                return False
        return len(stack) == 0
            
        