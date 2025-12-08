class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use a for loop to traverse the grid
        # implement a helper function which uses breadth first to explore and mark the visited land area
        # from the for, increement the counter everytime I come across unvisited land
        # record the visited land in a seen set

        seen = set()
        count = 0

        rows = len(grid)
        cols = len(grid[0])

        def helper(row, col):
            if ((row, col)) in seen:
                return
            
            if not 0 <= row < rows or not 0 <= col < cols:
                return
            
            if grid[row][col] == "0":
                return
            
            seen.add((row, col))

            helper(row + 1, col)
            helper(row - 1, col)
            helper(row, col + 1)
            helper(row, col - 1)

        
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and grid[row][col] == "1":
                    count += 1
                    helper(row, col)
        
        return count

        