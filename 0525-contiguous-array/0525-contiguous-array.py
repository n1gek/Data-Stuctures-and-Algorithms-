class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        # top_score = 0

        # for x in range(len(nums)):
        #     left = x
        #     one_count = 0
        #     zero_count = 0

        #     while left < len(nums):
        #         if nums[left] == 1:
        #             one_count += 1
        #         else:
        #             zero_count += 1
                
        #         if one_count == zero_count:
        #             length = left - x + 1
        #             top_score = max(top_score, length)
        #         left += 1
                
                
        # return top_score
        balance = 0
        balance_map = {0:-1}
        length = 0
        #[1, 0]

        for i, num in enumerate(nums):
            if num == 1:
                balance += 1
            else:
                balance -= 1
            
            if balance in balance_map:
                length = max(length, i - balance_map[balance])
            else:
                balance_map[balance] = i
        
        return length


                    



        

        