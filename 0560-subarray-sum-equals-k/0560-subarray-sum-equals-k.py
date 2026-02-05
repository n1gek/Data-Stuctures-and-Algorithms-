from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        counts = defaultdict(int)
        counts[0] = 1
        curr = 0
        total = 0

        for num in nums:
            curr += num

            need = curr - k
            if need in counts:
                occurences = counts[need]
                total += occurences
            

            counts[curr] += 1
        
        return total


        