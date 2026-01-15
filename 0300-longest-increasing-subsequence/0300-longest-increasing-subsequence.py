class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # use dynamic programming

        memo = {}

        def helper(i):          
            res = 1

            if i in memo:
                return memo[i]

            for j in range(i):
                if nums[i] > nums[j]:
                    res = max(res, helper(j) + 1)
            
            memo[i] = res

            return res
        
        return max(helper(i) for i in range(len(nums)))

