class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # binary search
        left = 0
        right = len(nums) -1

        # [1....5....8] target 5
        # [4.....7.....2] target 7
        # [9....4......8] target 4

        while left <= right:
            mid = (left + right) // 2 

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]: # check to see if left side is sorted
                if nums[left] <= target < nums[mid]: # check to see if target lies in this range
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if nums[mid] < target <= nums[right]: # check to see if target lies on the other half
                    left = mid + 1
                else:
                    right = mid - 1
            
        
        return -1