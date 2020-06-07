'''
5430. Design Browser History

You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
'''


class BrowserHistory:

    def __init__(self, homepage: str):
        self.backward = []
        self.forwards = []
        self.current = homepage

    def visit(self, url: str) -> None:
        self.backward.append(self.current)
        self.forwards = []
        self.current = url
        return None

    def back(self, steps: int) -> str:
        if len(self.backward) <= steps:
            try:
                self.current = self.backward[0]
            except:
                pass
            try:
                self.forwards = self.backward[1:] + self.forwards
            except:
                pass
            self.backward = []
        else:
            self.current = self.backward[-steps]
            try:
                self.forwards = self.backward[-steps + 1:] + self.forwards
            except:
                pass
            try:
                self.backward = self.backward[:-steps]
            except:
                pass
        return self.current

    def forward(self, steps: int) -> str:
        if len(self.forwards) <= steps:
            try:
                self.current = self.forwards[-1]
            except:
                pass
            try:
                self.backward = self.backward + self.forwards[:-1]
            except:
                pass
            self.forwards = []
        else:
            self.current = self.forwards[steps]
            try:
                self.backward = self.backward + self.forwards[:steps]
            except:
                pass
            try:
                self.forwards = self.forwards[steps + 1:]
            except:
                pass
        return self.current


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

obj = BrowserHistory("leetcode.com")
print(obj.visit("google.com"))
print(obj.visit("facebook.com"))
print(obj.visit("youtube.com"))
print(obj.back(1))
print(obj.back(1))
print(obj.forward(1))
print(obj.visit("linkedin.com"))
print(obj.forward(2))
print(obj.back(2))
