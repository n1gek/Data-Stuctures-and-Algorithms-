from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a dictionary, sorted word as key
        # use the sorted word as key
        # iterate the list
        # if the key already exists, append the word to the values
        # else make a new key,val pair

        res = defaultdict(list)

        for word in strs:
            res["".join(sorted(word))].append(word)
        
        print(res)
        output = []
        for key, val in res.items():
            output.append(val)

        return output
