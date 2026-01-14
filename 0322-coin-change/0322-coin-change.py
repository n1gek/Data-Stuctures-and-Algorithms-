class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def helper(curr):
            if curr == 0:
                return 0
            if curr < 0:
                return float("inf")
            
            if curr in memo:
                return memo[curr]
            
            best = float("inf")
            
            for c in coins:
                res = helper(curr - c)
                if res != float("inf"):
                    best = min(best, res + 1)
            
            memo[curr] = best
            return best

        
        ans = helper(amount)

        return ans if ans != float("inf") else -1

            

