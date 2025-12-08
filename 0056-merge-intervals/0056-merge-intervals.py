class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals based off the starting time

        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            s, e = intervals[i]

            prevS, prevE = res[-1]

            if prevE >= s:
                res.pop()
                res.append([prevS, e])
            else:
                res.append(intervals[i])
        
        print(res)
        return res