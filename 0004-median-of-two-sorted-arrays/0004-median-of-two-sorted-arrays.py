class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = []

        left = right = 0 # iterators for 2 different lists

        while left < len(nums1) and right < len(nums2):
            if nums1[left] <= nums2[right]:
                new_arr.append(nums1[left])
                left += 1
            else:
                new_arr.append(nums2[right])
                right += 1
        
        # check if either list wasnt exhausted and append the remainders to the main list
        if left < len(nums1):
            new_arr.extend(nums1[left:])
        elif right < len(nums2):
            new_arr.extend(nums2[right:])

        length = len(new_arr)
        print(new_arr)
        if length % 2 != 0: # odd
            mid = length // 2
         
            return new_arr[mid]
        else:
            mid = length // 2
            print(f'mid {mid}')
            return (new_arr[mid] + new_arr[mid - 1]) / 2