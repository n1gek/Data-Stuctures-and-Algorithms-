class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # backtracking/recursion
        res = []

        def helper(path, pre, post):
            if len(path) == n * 2:
                res.append(path)
                return
            
            open = "("
            close = ")"
            if pre < n:
                new = path + open
                helper(new, pre + 1, post)
            if post < pre:
                new = path + close
                helper(new,pre, post + 1)
        
        helper("", 0, 0)

        return res

            
