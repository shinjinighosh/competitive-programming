class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        concat = lambda x: "".join(x)
        return concat(word1) == concat(word2)
