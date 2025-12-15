class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
        L = len(n)
        num = int(n) 

        # compute left correctly
        left_len = (L + 1) // 2
        left = n[:left_len]

        # helper to mirror
        def helper(s):
            if L % 2 == 0:
                return s + s[::-1]
            else:
                return s + s[:-1][::-1]

        candidates = set()

        # base palindrome
        candidates.add(helper(left))

        # left - 1
        left_minus = str(int(left) - 1)
        candidates.add(helper(left_minus))

        # left + 1
        left_plus = str(int(left) + 1)
        candidates.add(helper(left_plus))

        # edge cases
        candidates.add("9" * (L - 1))
        candidates.add("1" + "0"*(L-1) + "1")

        # remove original number if present
        candidates.discard(n)

        best = None
        diff = float("inf")

        for cand in candidates:
            if not cand:
                continue
            val = int(cand)
            d = abs(val - num)
            if d < diff or (d == diff and val < int(best)):
                diff = d
                best = cand

        return best