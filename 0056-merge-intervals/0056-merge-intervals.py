class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        stack = [intervals[0]]

        for x in intervals[1:]:
            start, end =stack[-1] #1, 3
            cstart, cend = x #2, 6 end > cstart

            if end >= cstart:
                stack.pop()
                stack.append([min(start, cstart), max(cend, end)])
            
            else:
                stack.append(x)
        return stack
