class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        start = 0
        count = 0
        seen = defaultdict(int)

        for end in range(len(s)):
            seen[s[end]] += 1
            count = max(count, seen[s[end]])
            while len(seen) > 1 and (end - start + 1) - count > k:
                seen[s[start]] -= 1
                start += 1
            best = max(best, end - start + 1)

        return best