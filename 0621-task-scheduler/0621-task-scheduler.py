from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        heap = []
        for task, val in count.items():
            heap.append((-val, task))
        
        heapq.heapify(heap)

        intervals = 0
        # heap = [(-3, A), (-3, B)]

        while heap:
            temp = []

            cycles = n + 1

            for _ in range(cycles):
                if heap:
                    freq, task = heapq.heappop(heap)
                    freq += 1

                    if freq != 0:
                        temp.append((freq, task))
                intervals += 1

                if not heap and not temp:
                    break
                
            for item in temp:
                heapq.heappush(heap, item)
        
        return intervals
                    





