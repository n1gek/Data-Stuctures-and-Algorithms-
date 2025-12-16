from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # user a counter to count the elements
        count = Counter(nums)

        nums = [(-freq, val) for val, freq in count.items()]

        heapq.heapify(nums)

        res = []

        for _ in range(k):
            freq, val = heapq.heappop(nums)
            res.append(val)

        return res
