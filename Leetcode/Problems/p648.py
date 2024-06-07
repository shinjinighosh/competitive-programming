class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dic = set(dictionary)
        res = []
        for word in sentence.split():
            for idx in range(len(word)):
                if word[:idx] in dic:
                    res.append(word[:idx])
                    break
            else:
                res.append(word)
        return " ".join(res)
