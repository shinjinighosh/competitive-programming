class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ctr = 0
        if ruleKey == "color":
            idx = 1
        elif ruleKey == "type":
            idx = 0
        else:
            idx = 2

        for item in items:
            if item[idx] == ruleValue:
                ctr += 1
        return ctr
