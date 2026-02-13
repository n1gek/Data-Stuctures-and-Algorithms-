class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        # dynamic programming

        def helper(curr): # takes in the current amount
            if curr == 0:
                return 0
            if curr < 0:
                return float("inf")
            
            if curr in memo:
                return memo[curr]
            
            best = float("inf")
            for c in coins:
                res = helper(curr - c) # recurrence relation: we compute how many ways to build the smaller coin'
                if res != float("inf"):
                    best = min(best, res + 1)
            
            memo[curr] = best
            return best
        
        result = helper(amount)

        if result == float("inf"):
            return -1
        else:
            return result


        