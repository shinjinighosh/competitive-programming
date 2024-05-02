class Solution:
    def sortSentence(self, s: str) -> str:
        ordered_words = [" " for _ in range(len(s.split()))]
        for word in s.split():
            pos = int(word[-1]) - 1
            ordered_words[pos] = word[:-1]
        return " ".join(ordered_words)
        
