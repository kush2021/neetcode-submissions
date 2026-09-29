class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "|"
        for c in s:
            t += c
            t += "|"

        p = [0 for _ in range(len(t))]
        best = 0

        for i in range(1, len(t) - 1):
            j = 1
            while i - j >= 0 and i + j < len(t) and t[i - j] == t[i + j]:
                j += 1
            p[i] = j - 1
            if p[i] > p[best]:
                best = i

        res = t[best - p[best]:best + p[best] + 1]
        return res.replace("|", "")