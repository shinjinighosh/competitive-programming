# Stream of Characters

'''
Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
'''


class TrieNode:
    def __init__(self):
        self.children, self.end_node = {}, 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = 1


class StreamChecker:
    def __init__(self, words):
        self.trie = Trie()
        self.Stream = deque()
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter):
        self.Stream.appendleft(letter)
        cur = self.trie.root
        for c in self.Stream:
            if c in cur.children:
                cur = cur.children[c]
                if cur.end_node:
                    return True
            else:
                break
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
