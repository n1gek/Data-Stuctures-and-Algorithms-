class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        memo = {
            "(": ")",
            "[": "]",
            "{":"}"
        }

        for char in s:
            if char in memo:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if memo[top] != char:
                    return False
        
        return len(stack) == 0

        