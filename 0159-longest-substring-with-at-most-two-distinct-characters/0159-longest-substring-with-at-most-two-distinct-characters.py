class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        freq = {}
        left = 0
        res = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            while len(freq) > 2:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
                
            res = max(res, right - left + 1)
            # {e:2, c:1, b:1}
        
        return res
            

            
