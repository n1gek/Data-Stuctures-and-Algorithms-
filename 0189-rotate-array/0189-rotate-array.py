class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # reverse the entire arr [7, 6, 5 ,4 , 3, 2 ,1]
        k = k % len(nums)
        nums.reverse()

        nums[:k] = reversed(nums[:k])

        nums[k:] = reversed(nums[k:])


        