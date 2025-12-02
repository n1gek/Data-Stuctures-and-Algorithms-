class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use the complement method

        hashmap = {}

        for index, num in enumerate(nums):

            if num in hashmap:
                return [hashmap[num], index]

            diff = target - num #7

            hashmap[diff] = index
        
        print(hashmap)


