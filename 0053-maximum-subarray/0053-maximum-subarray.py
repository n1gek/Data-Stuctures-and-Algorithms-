class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # plug in that Kadane's algorithm
        curr_sum = 0
        total = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            total = max(total, curr_sum)
        
        return total

        