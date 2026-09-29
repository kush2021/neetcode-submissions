class Solution:
    def countSubstrings(self, s: str) -> int:
        t = "#"
        for c in s:
            t += c
            t += "#"
        
        p = [0 for _ in range(len(t))]

        for i in range(1, len(t) - 1):
            j = 1
            while i - j >= 0 and i + j < len(t) and t[i - j] == t[i + j]:
                j += 1
            p[i] = j // 2

        return sum(p)