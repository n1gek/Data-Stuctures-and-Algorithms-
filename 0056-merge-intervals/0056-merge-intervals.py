class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals based off the starting time
        intervals.sort(key=lambda x: x[0])
        # conditions for merging
        #1 if the second starting time <= first ending time
        #2 

        stack = []

        for ival in intervals:
            if not stack:
                stack.append(ival)
            else:
            
                start, end = stack[-1] #[0, 0]
                currStart, currEnd = ival #[1, 4]

                if currStart <= end:
                    newVal = [min(start, currStart), max(end, currEnd)]
                    stack.pop()
                    stack.append(newVal)
                else:
                    stack.append(ival)
        
        return stack