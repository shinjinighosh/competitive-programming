# 208. Implement Trie (Prefix Tree)

'''
Implement a trie with insert, search, and startsWith methods.
'''


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.T = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.T
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = None

    def match(self, seq, prefix):
        node = self.T
        for c in seq:
            if c not in node:
                return False
            node = node[c]
        return True if prefix else '$' in node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.match(word, False)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.match(prefix, True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
