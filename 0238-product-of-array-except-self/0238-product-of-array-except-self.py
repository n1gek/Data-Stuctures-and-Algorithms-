class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        '''
        nums = [1, 2, 3, 4], res = [1,1,1,1]
        prefix = 2
        res = [1, 1, 2, 

        
        '''
        res = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        

        post = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res