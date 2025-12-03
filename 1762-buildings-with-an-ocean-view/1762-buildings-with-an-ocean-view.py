class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # start iterating from the right
        # rightmost building has the ocean view
        # keep a height pointer that tracks the tallest building seen so far
        # compare tallest building to new building 

        highest = heights[-1]
        last = len(heights) - 1
        res = [last]

        for i in range(len(heights) - 1,-1,-1):
            if heights[i] > highest:
                print(f'{heights[i]} is greater than {highest}')
                res.append(i)
                highest = heights[i]
        
        return res[::-1]

