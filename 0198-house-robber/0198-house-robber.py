class Solution:
    def rob(self, nums: List[int]) -> int:

        #dynamic programming

        def helper(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[1], nums[0])
            
            if i in memo:
                return memo[i]
            
            memo[i] = max((nums[i] + helper(i-2)), helper(i - 1))

            return memo[i]
        
        memo = {}
        
        res = 0
        for i in range(len(nums)):
            res = max(res, helper(i))
        
        return helper(len(nums) - 1)

