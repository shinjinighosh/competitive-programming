# Iterator for Combination

'''
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
'''

from os.path import commonprefix


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.c = characters
        self.l = combinationLength
        self.state = ""

    def next(self) -> str:
        if self.state == "":  # start off
            self.state = self.c[:self.l]
        else:
            end = len(commonprefix([self.c[::-1], self.state[::-1]]))
            place = self.c.index(self.state[-end - 1])
            self.state = self.state[:-end - 1] + self.c[place + 1: place + 2 + end]
        return self.state

    def hasNext(self) -> bool:
        return self.state != self.c[-self.l:]


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
