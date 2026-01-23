from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        vals = []
        # {1:3, 2:2, 3:1}

        for key, count in count.items():
            vals.append((-count, key))
        
        heapq.heapify(vals)
        print(vals)
        
        res = []
        for i in range(k):
            val = heapq.heappop(vals)
            res.append(val[1])
        
        return res


