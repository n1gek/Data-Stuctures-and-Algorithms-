class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        seen = set()

        def helper(row, col, index):
            if index == len(word):
                return True
            
            if not 0 <= row < rows or not 0 <= col < cols:
                return False
            if (row, col) in seen:
                return False
            if board[row][col] != word[index]:
                return False
            seen.add((row, col))
            
            res = (helper(row + 1, col, index + 1) or
            helper(row - 1, col, index + 1) or
            helper(row, col + 1, index + 1) or
            helper(row, col - 1, index + 1))

            seen.remove((row, col))

            return res
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen:
                    if helper(row, col, 0):
                        return True
        
        return False

