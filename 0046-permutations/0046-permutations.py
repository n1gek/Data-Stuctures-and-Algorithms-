class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def helper(arr):
            if len(arr) == len(nums):
                res.append(arr[:])
                return
            
            for num in nums:
                if num not in arr:
                    arr.append(num)
                    helper(arr)
                    arr.pop()
        
        helper([])

        return res