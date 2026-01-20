class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = float("inf")
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            res = min(res, nums[mid])

            if nums[left] <= nums[mid]: # left side is sorted
                if nums[left] <= nums[mid] < nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            elif nums[mid] <= nums[right]: # right side is sorted
                if nums[left] < nums[mid] <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                break
        
        return res
        # left = 2
        #right = 3
        # mid = 2
            
        