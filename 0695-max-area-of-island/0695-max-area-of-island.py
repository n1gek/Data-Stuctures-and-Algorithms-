class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def helper(row, col):
            rowInbound = 0 <= row < rows
            colInbound = 0 <= col < cols

            if not rowInbound or not colInbound:
                return 
            if (row, col) in seen:
                return 
            if grid[row][col] == 0:
                return 
            
            seen.add((row, col))

            helper(row + 1, col)
            helper(row - 1, col)
            helper(row, col + 1)
            helper(row, col - 1)
            
  
        count = 0
        seen = set()
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and grid[row][col] == 1:
                    helper(row, col)
                    count += 1
        
        return count
        
        