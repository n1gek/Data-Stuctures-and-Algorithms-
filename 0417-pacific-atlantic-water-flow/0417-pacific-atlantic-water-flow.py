class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def helper(row, col, visited):
            rowInbound = 0 <= row < rows
            colInbound = 0 <= col < cols

            if not rowInbound or not colInbound:
                return
            if (row, col) in visited:
                return

            visited.add((row, col))

            # explore only if next cell is >= current cell
            curr = heights[row][col]

            # down
            if row + 1 < rows and heights[row + 1][col] >= curr:
                helper(row + 1, col, visited)
            # up
            if row - 1 >= 0 and heights[row - 1][col] >= curr:
                helper(row - 1, col, visited)
            # right
            if col + 1 < cols and heights[row][col + 1] >= curr:
                helper(row, col + 1, visited)
            # left
            if col - 1 >= 0 and heights[row][col - 1] >= curr:
                helper(row, col - 1, visited)

        # Pacific: top row + left column
        for c in range(cols):
            helper(0, c, pacific)
        for r in range(rows):
            helper(r, 0, pacific)

        # Atlantic: bottom row + right column
        for c in range(cols):
            helper(rows - 1, c, atlantic)
        for r in range(rows):
            helper(r, cols - 1, atlantic)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res