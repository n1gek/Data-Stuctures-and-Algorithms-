class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        memo = {}
        left = 0
        res = 0

        for right in range(len(s)):
            memo[s[right]] = memo.get(s[right], 0) + 1

            while len(memo) > k:
                memo[s[left]] -= 1
                if memo[s[left]] == 0:
                    del memo[s[left]]
                left += 1
            
            res = max(res, right - left + 1)

        return res