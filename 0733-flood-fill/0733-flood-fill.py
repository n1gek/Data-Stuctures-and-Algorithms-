class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        '''
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
        '''
        rows = len(image)
        cols = len(image[0])
        val = image[sr][sc]

        def helper(row, col, seen):

            rowInbound = 0 <= row < rows
            colInbound = 0 <= col < cols

            if not rowInbound or not colInbound:
                return
            
            if (row, col) in seen:
                return
            
            if image[row][col] != val:
                seen.add((row, col))
                return
            
            seen.add((row, col))

            image[row][col] = color

            helper(row + 1, col, seen)
            helper(row - 1, col, seen)
            helper(row, col - 1, seen)
            helper(row, col + 1, seen)
        
        helper(sr, sc, set())

        return image






        