class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix = []
        self.running_sum = 0
        for n in self.w:
            self.running_sum += n
            self.prefix.append(self.running_sum)
        self.total = self.running_sum
        

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)

        left, right = 0, len(self.w) - 1

        while left < right:
            mid = (left + right) // 2

            if self.prefix[left] < target:
                left += 1
            else:
                right = mid
        
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()