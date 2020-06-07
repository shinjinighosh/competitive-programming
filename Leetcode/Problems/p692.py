# 692. Top K Frequent Words


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequencies = {}
        unique_words = []
        for word in words:
            if word not in frequencies:
                frequencies[word] = 1
                unique_words.append(word)
            else:
                frequencies[word] += 1

        # to sort with one key normal and other reverse
        return sorted(unique_words, key=lambda x: (1 / frequencies[x], x))[:k]
