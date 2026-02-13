class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for num in nums:
            index = abs(num) - 1
            nums[index] = abs(nums[index]) * -1
        
        print(nums)
        res = []

        for i, n in enumerate(nums):
            if n > 0:
                num = i + 1
                res.append(num)
        
        return res

        