class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {s:chr(ord('a')+i) for i,s in enumerate(order)}
        return words == sorted(words, key=lambda word : ''.join(order_dict[s] for s in word))