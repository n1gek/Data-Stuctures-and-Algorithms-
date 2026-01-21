class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        print(intervals)

        stack = []

        for ival in intervals:
            if not stack:
                stack.append(ival)
            else:
                start, end = stack[-1]
                currStart, currEnd = ival

                if currStart <= end:
                    newVal = [min(start, currStart), max(end, currEnd)]
                    stack.pop()
                    stack.append(newVal)
                else:
                    stack.append(ival)
        
        return stack
        