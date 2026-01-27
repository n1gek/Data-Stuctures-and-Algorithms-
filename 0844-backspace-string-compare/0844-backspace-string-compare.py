class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def removePound(word):
            stack = []

            for char in word:
                if char.isalpha():
                    stack.append(char)
                elif char == "#":
                    if stack:
                        stack.pop()
            
            return "".join(stack)
        
        return removePound(s) == removePound(t)
        