class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        trie = Trie()
        for i, word in enumerate(words):
            trie.add(word, i)

        def search(i, j, seen, node=None):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in seen:
                return

            c = board[i][j]
            if node is None:
                node = trie.root
            if c in node.children:
                node = node.children[c]
            else:
                return

            if node.is_end and node.i != -1:
                results.append(words[node.i])
                node.i = -1

            seen.add((i, j))
            search(i - 1, j, seen, node)
            search(i + 1, j, seen, node)
            search(i, j - 1, seen, node)
            search(i, j + 1, seen, node)
            seen.remove((i, j))

        results = []
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                search(i, j, set())
        return results

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word, i):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True
        cur.i = i

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.i = -1