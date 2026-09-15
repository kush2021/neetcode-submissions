class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freq = {}
        for c in t:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
        
        shortest = ""
        best = float("inf")
        seen = {}
        start = 0
        have = 0
        need = len(freq)
        for end in range(len(s)):
            if s[end] in freq:
                if s[end] in seen:
                    seen[s[end]] += 1
                else:
                    seen[s[end]] = 1
                
                if seen[s[end]] == freq[s[end]]:
                    have += 1

            while have == need:
                if end - start + 1 < best:
                    best = end - start + 1
                    shortest = s[start:end + 1]

                left = s[start]
                if left in freq:
                    seen[left] -= 1
                    if seen[left] < freq[left]:
                        have -= 1

                start += 1

        return shortest