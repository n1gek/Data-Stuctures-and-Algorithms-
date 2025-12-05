class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a 2 pointer approach
        # set left which stays still
        # initiate right which moves rightways and counts unique chars

        left = 0
        res = 0

        seen = set()

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
                
            seen.add(s[right])
            res = max(res, right - left + 1)
        
        return res


        
        