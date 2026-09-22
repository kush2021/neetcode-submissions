class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c != '.' and c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, pos):
            if pos == len(word):
                return node.is_end

            c = word[pos]
            if c in node.children:
                return dfs(node.children[c], pos + 1)
            elif c == '.':
                for char, child in node.children.items():
                    match = dfs(child, pos + 1)
                    if match:
                        return True
            return False
        
        return dfs(self.root, 0)
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False