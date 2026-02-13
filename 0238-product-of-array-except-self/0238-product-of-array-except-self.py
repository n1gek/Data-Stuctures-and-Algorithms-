class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        #[1, 1, 2, 6]
        postfix = 1
        n = len(nums)

        for i in range(n - 1, -1, -1):
            result[i] = postfix * result[i]
            postfix *= nums[i]
        
        return result

        # this solution incorporates 2 loops
        # the first loop computes everything to the left of a particular index: prefix is the product of everything left
        # the second loop, computes everything to the right of the current index: product of everything right
        # the second loop computes the product of prefix and psotfix
