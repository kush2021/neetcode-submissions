class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            l = str(len(word))
            l2 = str(len(l))
            s = s + l2 + l + word
        return s

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        l = 0
        strs = []
        while l < len(s):
            i = l + 1
            j = int(s[l])
            l2 = int(s[i:i + j])
            strs.append(s[i + j:i + j + l2])
            l = i + j + l2

        return strs