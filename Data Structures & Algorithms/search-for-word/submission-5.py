class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = word[0]

        def search(i: int, j: int, pos: int, seen: set[tuple(int, int)]) -> bool:
            if pos == len(word):
                return True
            
            nxt = word[pos]
            if i > 0 and (i - 1, j) not in seen and board[i - 1][j] == nxt:
                seen.add((i - 1, j))
                if search(i - 1, j, pos + 1, seen):
                    return True
                seen.remove((i - 1, j))
            if i + 1 < len(board) and (i + 1, j) not in seen and board[i + 1][j] == nxt:
                seen.add((i + 1, j))
                if search(i + 1, j, pos + 1, seen):
                    return True
                seen.remove((i + 1, j))
            if j > 0 and (i, j - 1) not in seen and board[i][j - 1] == nxt:
                seen.add((i, j - 1))
                if search(i, j - 1, pos + 1, seen):
                    return True
                seen.remove((i, j - 1))
            if j + 1 and (i, j + 1) not in seen and j + 1 < len(board[0]) and board[i][j + 1] == nxt:
                seen.add((i, j + 1))
                if search(i, j + 1, pos + 1, seen):
                    return True
                seen.remove((i, j + 1))
            
            return False

        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter == start and search(i, j, 1, {(i, j)}):
                    return True
        
        return False