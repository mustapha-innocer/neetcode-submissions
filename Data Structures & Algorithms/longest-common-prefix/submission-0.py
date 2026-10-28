class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = strs[0]
        for s in strs:
            if len(s) < len(shortest):
                shortest = s
        longest_prefix = ""
        for i, c in enumerate(shortest):
            for s in strs:
                if s[i] != c:
                    return longest_prefix
            longest_prefix += c
        return longest_prefix