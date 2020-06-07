'''
5430. Design Browser History

You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
'''

# CHANGE TO USE JUST ONE QUEUE with a pointer


class BrowserHistory:

    def __init__(self, homepage: str):
        self.backward = []
        self.forwards = []
        self.current = homepage
        print(f"Current {self.current} backward {self.backward} forward {self.forwards}")

    def visit(self, url: str) -> None:
        self.backward.append(self.current)
        self.forwards = []
        self.current = url
        print(f"Current {self.current} backward {self.backward} forward {self.forwards}")
        return None

    def back(self, steps: int) -> str:
        if len(self.backward) <= steps:
            self.forwards.append(self.current)
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
            # print("taking this route")
            self.forwards.append(self.current)
            self.current = self.backward[-steps]
            try:
                if steps != 1:
                    self.forwards = self.backward[-steps + 1:] + self.forwards
            except:
                pass
            try:
                self.backward = self.backward[:-steps]
            except:
                pass

        print(f"Current {self.current} backward {self.backward} forward {self.forwards}")
        return self.current

    def forward(self, steps: int) -> str:
        if len(self.forwards) <= steps:
            self.forwards.append(self.current)
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
            self.forwards.append(self.current)
            self.current = self.forwards[steps]
            try:
                self.backward = self.backward + self.forwards[:steps]
            except:
                pass
            try:
                self.forwards = self.forwards[steps + 1:]
            except:
                pass
        print(f"Current {self.current} backward {self.backward} forward {self.forwards}")
        return self.current


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

print("Starting at leetcode")
obj = BrowserHistory("leetcode.com")
print("visiting google")
print(obj.visit("google.com"))
print("visiting facebook")
print(obj.visit("facebook.com"))
print("visiting youtube")
print(obj.visit("youtube.com"))
print("go back 1")
print(obj.back(1))
print("go back 1")
print(obj.back(1))
# print("go forward 1")
# print(obj.forward(1))
# print(obj.visit("linkedin.com"))
# print(obj.forward(2))
# print(obj.back(2))
# print(obj.back(7))

# expected: [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
