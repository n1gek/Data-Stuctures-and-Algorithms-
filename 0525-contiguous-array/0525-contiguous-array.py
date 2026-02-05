class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        count = {0:-1}
        balance = 0
        res = 0

        for i, num in enumerate(nums):
            if num == 1:
                balance += 1
            else:
                balance -= 1
            
            if balance in count:
                length = i - count[balance]
                res = max(res, length)
            else:
                count[balance] = i 
        
        return res

