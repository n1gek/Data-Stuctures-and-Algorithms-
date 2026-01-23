import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        print(stones)
        heapq.heapify(stones)

        while len(stones) > 1:
            q, p = heapq.heappop(stones), heapq.heappop(stones)
            if q == p:
                continue
            else:
                if q > p:
                    val = q - p
                else:
                    val = p - q
                heapq.heappush(stones, -val)
        
        if not stones:
            return 0
        else:
            return -stones[0]

        