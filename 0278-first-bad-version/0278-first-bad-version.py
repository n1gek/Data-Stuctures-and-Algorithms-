# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        #[1, 2, 3, 4, 5, 6]
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid): #if True: Falted, search left half
                right = mid - 1
            else:
                left = mid + 1
            
        
        return left