class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = {}
        left = 0
        highest = 0
        ans = 0

        for right in range(len(s)):
            letters[s[right]] = letters.get(s[right], 0) + 1
            highest = max(highest, letters[s[right]])

            window_length = right - left + 1
            replacements = window_length - highest

            while replacements > k:
                letters[s[left]] -= 1
                if letters[s[left]] == 0:
                    del letters[s[left]]
                left += 1

                window_length = right - left + 1
                replacements = window_length - highest

            ans = max(ans, window_length)

        return ans
