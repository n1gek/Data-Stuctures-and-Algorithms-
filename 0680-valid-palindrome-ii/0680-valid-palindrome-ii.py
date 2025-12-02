class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1 #2

        while left < right:

            if s[left] == s[right]:
                left += 1
                right -= 1
            
            else:
                new1 = s[left + 1: right + 1]
                new2 = s[left:right]

                if new1 == new1[::-1]:
                    print(right)
                    print(left + 1)
                    print(new1)
                    print(new1[::-1])
                    print("new1")
                    return True
                
                elif new2 == new2[::-1]:
                    print("new2")
                    return True
                
                else:
                    return False
        
        return True
        
        

        