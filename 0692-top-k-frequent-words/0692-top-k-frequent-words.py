from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        count = Counter(words)

        freq = sorted(count.keys(), key=lambda x: (-count[x], x))
        # freq = ['i', 'love', 'leetcode', 'coding']


        return freq[:k]
        