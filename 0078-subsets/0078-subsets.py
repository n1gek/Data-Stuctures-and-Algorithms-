class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # for each element, append the element to the list
        # append the rest of the cases without the element 

        def helper(arr, index):
            res.append(arr[:])

            for i in range(index, len(nums)):
                arr.append(nums[i])
                helper(arr, i+1)
                arr.pop()
        
        res = []
        arr = []
        helper(arr, 0)

        return res
