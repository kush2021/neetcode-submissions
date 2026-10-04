class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        cache = {"": True}

        def split(s):
            if s in cache:
                return cache[s]
            
            for i in range(len(s)):
                segment = s[0:i + 1]
                if segment in words and split(s[i + 1:]):
                    cache[s] = True
                    return True
            
            cache[s] = False
            return False

        return split(s)