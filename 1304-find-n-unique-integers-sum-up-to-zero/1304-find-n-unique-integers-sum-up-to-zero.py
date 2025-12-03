class Solution:
    def sumZero(self, n: int) -> List[int]:
        # given an integer n
        # find n unique integers that add up to 0
        # return any array
        res= []
        #n = 4


        for i in range(1, n//2 + 1):
            res.append(i)
            res.append(-i)
        
        if n % 2 != 0:
            res.append(0)
        
        return res


