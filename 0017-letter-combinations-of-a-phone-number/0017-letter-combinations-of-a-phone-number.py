from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # backtracking

        nums = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

        def helper(digits, path, res, index):
            if index == len(digits):
                res.append(path)
                return
            
            letters = nums[digits[index]] 
            
            for letter in letters:
                new_path = path + letter
                helper(digits, new_path, res, index + 1)
        
        res = []
        helper(digits, "", res, 0)

        return res
   



        
        
        
        