class Solution:
    def romanToInt(self, s: str) -> int:

        hashmap = {
            "I":1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D":500,
            "M":1000
        }

        i = len(s) - 1
        total = 0

        while i >= 0:
            if i < len(s) - 1:
                if hashmap[s[i]] < hashmap[s[i + 1]]:
                    total -= hashmap[s[i]]
                else:
                    total += hashmap[s[i]]
            else:
                total += hashmap[s[i]]
            
            print(total)
            i -= 1
        
        return total

            


