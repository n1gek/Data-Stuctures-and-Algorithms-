class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for num in nums:
            index = abs(num) - 1
            nums[index] = abs(nums[index]) * -1
        
        print(nums)
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                n = i + 1
                res.append(n)
        
        return res