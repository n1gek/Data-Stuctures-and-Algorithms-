class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print(candidates)

        res = []

        def helper(arr, index, total):
            if total == target:
                res.append(arr[:])
                return
            
            if total > target:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                total += candidates[i]
                arr.append(candidates[i])
                helper(arr, i + 1, total)
                total -= candidates[i]
                arr.pop()
        
        helper([], 0, 0)

        return res
            


        