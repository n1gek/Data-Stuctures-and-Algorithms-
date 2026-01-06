class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def helper(i):
            ans = 1

            if i in memo:
                return memo[i]
            
            for j in range(i):
                if nums[i] > nums[j]:
                    ans = max(ans, helper(j) + 1)
            
            memo[i] = ans

            return ans
        
        memo = {}

        return max(helper(i) for i in range(len(nums)))