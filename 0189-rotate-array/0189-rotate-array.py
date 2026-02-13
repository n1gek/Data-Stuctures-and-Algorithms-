class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        # 3%7 = 3
        # 3// 7 = 0
        k = k % len(nums) # so that you dont rotate more than necessary if k=10 and n=3: its the same as rotating by 3
        nums.reverse() #[7,6,5,4,3,2,1]

        nums[k:] = reversed(nums[k:])
        nums[:k] = reversed(nums[:k])



        print(nums)




        