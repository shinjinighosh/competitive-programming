class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        num_words = lambda x: len(x.split(" "))
        return max([num_words(sent) for sent in sentences])
        
