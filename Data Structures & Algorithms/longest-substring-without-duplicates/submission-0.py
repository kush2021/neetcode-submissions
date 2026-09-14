class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        best = 0
        start = 0

        for end in range(len(s)):
            if s[end] in seen:
                start = max(seen[s[end]] + 1, start)
            best = max(best, end - start + 1)
            seen[s[end]] = end

        return best