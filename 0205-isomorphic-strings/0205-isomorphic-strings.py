from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        
        if len(s) != len(t):
            return False
        
        mapp = {}

        for i in range(len(s)):
            if s[i] not in mapp:
                mapp[s[i]] = t[i]
            elif t[i] not in mapp:
                mapp[t[i]] = s[i]
            

            elif s[i] in mapp:            
                if mapp[s[i]] != mapp[t[i]]:
                    return False
                
            elif t[i] in mapp:
                if mapp[t[i]] != mapp[s[i]]:
                    return False
        
        return True  

        