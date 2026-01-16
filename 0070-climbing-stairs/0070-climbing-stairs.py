class Solution:
    def climbStairs(self, n: int) -> int:
        # lets say we have 3 steps, in order to reach the third one, we can either start from step 1 and then step 3 or we can do step 1, 2 and then 3. or we can do step 2 and then 3
        # so for n = 3: answer is the number of ways to reach 1 and 2

        memo = {}

        def helper(i):
            if i <= 1:
                return 1
            
            if i in memo:
                return memo[i]
            
            memo[i] = helper(i - 1) + helper(i - 2)

            return memo[i]
        
        return helper(n)